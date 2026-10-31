/* KCO — runtime estático leve (substitui o motor do canvas do Claude) */
(function () {
  var handlers = [];
  var comp = null;
  var tplRoot = null;
  var app = null;
  var queued = false;
  var EXT = window.KCO_ASSET_EXT || {};
  var VOID = { area: 1, base: 1, br: 1, col: 1, embed: 1, hr: 1, img: 1, input: 1, link: 1, meta: 1, source: 1, track: 1, wbr: 1 };

  window.DCLogic = function DCLogic(props) { this.props = props || {}; this.state = {}; };
  window.DCLogic.prototype.setState = function (p) {
    Object.assign(this.state, typeof p === 'function' ? p(this.state) : p);
    schedule();
  };

  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
  function ev(expr, scope) {
    expr = expr.trim();
    if (expr === 'true') return true;
    if (expr === 'false') return false;
    var parts = expr.split('.');
    var v = scope[parts[0]];
    for (var i = 1; i < parts.length; i++) v = v == null ? undefined : v[parts[i]];
    return v;
  }
  function interp(str, scope) {
    return str.replace(/\{\{([\s\S]*?)\}\}/g, function (m, e) { var v = ev(e, scope); return v == null ? '' : String(v); });
  }
  function strip(v) { var m = /^\s*\{\{([\s\S]*)\}\}\s*$/.exec(v || ''); return m ? m[1] : v; }

  function render(node, scope, out) {
    if (node.nodeType === 3) { out.push(esc(interp(node.nodeValue, scope))); return; }
    if (node.nodeType !== 1 && node.nodeType !== 11) return;
    if (node.nodeType === 11) { kids(node, scope, out); return; }
    var tag = node.localName;
    if (tag === 'helmet') return;
    if (tag === 'sc-for') {
      var list = ev(strip(node.getAttribute('list')), scope) || [];
      var as = node.getAttribute('as');
      for (var i = 0; i < list.length; i++) { var s = Object.create(scope); s[as] = list[i]; kids(node, s, out); }
      return;
    }
    if (tag === 'sc-if') { if (ev(strip(node.getAttribute('value')), scope)) kids(node, scope, out); return; }
    out.push('<' + tag);
    for (var a = 0; a < node.attributes.length; a++) {
      var at = node.attributes[a], name = at.name, val = at.value;
      if (/^hint-/.test(name)) continue;
      if (/^on/.test(name) && /^\s*\{\{[\s\S]*\}\}\s*$/.test(val)) {
        var fn = ev(strip(val), scope);
        if (typeof fn === 'function') { handlers.push(fn); out.push(' data-on-' + name.slice(2) + '="' + (handlers.length - 1) + '"'); }
        continue;
      }
      out.push(' ' + name + '="' + esc(interp(val, scope)) + '"');
    }
    out.push('>');
    if (VOID[tag]) return;
    kids(node.content || node, scope, out);
    out.push('</' + tag + '>');
  }
  function kids(node, scope, out) { for (var c = node.firstChild; c; c = c.nextSibling) render(c, scope, out); }

  function fixAssets(html) {
    return html.replace(/\/_blob\/([0-9a-f]{32})/g, function (m, id) { return (window.KCO_ASSET_BASE || '') + 'assets/' + id + (EXT[id] || ''); });
  }

  /* diff mínimo: preserva vídeo, campos de formulário e rolagem */
  function patch(from, to) {
    if (from.nodeType !== to.nodeType || from.nodeName !== to.nodeName) { from.parentNode.replaceChild(to, from); return; }
    if (from.nodeType === 3) { if (from.nodeValue !== to.nodeValue) from.nodeValue = to.nodeValue; return; }
    if (from.nodeType !== 1) return;
    var tag = from.nodeName;
    var i, n;
    for (i = from.attributes.length - 1; i >= 0; i--) { n = from.attributes[i].name; if (!to.hasAttribute(n)) from.removeAttribute(n); }
    for (i = 0; i < to.attributes.length; i++) { n = to.attributes[i]; if (from.getAttribute(n.name) !== n.value) from.setAttribute(n.name, n.value); }
    if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT' || tag === 'VIDEO') return;
    var a = from.firstChild, b = to.firstChild;
    while (b) { var nb = b.nextSibling; if (!a) { from.appendChild(b); } else { var na = a.nextSibling; patch(a, b); a = na; } b = nb; }
    while (a) { var x = a.nextSibling; from.removeChild(a); a = x; }
  }

  function draw() {
    queued = false;
    handlers = [];
    var vals = comp.renderVals();
    var out = [];
    kids(tplRoot, vals, out);
    var html = fixAssets(out.join(''));
    var tmp = document.createElement('div');
    tmp.innerHTML = html;
    if (!app.firstChild) { while (tmp.firstChild) app.appendChild(tmp.firstChild); }
    else patch(app, (function () { var d = document.createElement('div'); d.id = app.id; while (tmp.firstChild) d.appendChild(tmp.firstChild); return d; })());
    var vids = app.querySelectorAll('video[autoplay]');
    for (var v = 0; v < vids.length; v++) { vids[v].muted = true; if (vids[v].paused) { var p = vids[v].play(); if (p && p.catch) p.catch(function () {}); } }
    var anyDialog = !!app.querySelector('[role="dialog"]');
    document.documentElement.style.overflow = anyDialog ? 'hidden' : '';
  }
  function schedule() { if (!queued) { queued = true; requestAnimationFrame(draw); } }

  function onEvent(e) {
    var el = e.target.closest ? e.target.closest('[data-on-' + e.type + ']') : null;
    if (!el || !app.contains(el)) return;
    var fn = handlers[+el.getAttribute('data-on-' + e.type)];
    if (fn) fn(e);
  }

  document.addEventListener('DOMContentLoaded', function () {
    tplRoot = document.getElementById('kco-template').content;
    app = document.getElementById('app');
    var props = {};
    try { var def = JSON.parse(document.getElementById('kco-props').textContent); for (var k in def) if (def[k] && 'default' in def[k]) props[k] = def[k].default; } catch (e) {}
    comp = new window.Component(props);
    ['click', 'input', 'change'].forEach(function (t) { app.addEventListener(t, onEvent); });
    document.addEventListener('keydown', function (e) {
      if (e.key !== 'Escape') return;
      var s = comp.state;
      if (s.contactOpen) comp.setState({ contactOpen: false });
      else if (s.priceOpen) comp.setState({ priceOpen: false });
      else if (s.openId) comp.setState({ openId: null });
    });
    draw();
  });
})();
