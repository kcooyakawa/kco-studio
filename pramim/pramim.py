# pra/mim para iPhone e iPad — roda dentro do a-Shell. powered by KCO Studio
# Uso: python ~/Documents/pramim.py <pedido>
#  <pedido> = base64 (vindo da página pra/mim) ou um link direto (vindo do menu Compartilhar)
import base64, json, os, re, sys

# Auto-atualização: busca a versão mais nova antes de rodar
if not os.environ.get("PRAMIM_ATUALIZADO"):
    try:
        import urllib.request
        novo = urllib.request.urlopen("https://kcooyakawa.github.io/kco-studio/pramim/pramim.py", timeout=6).read().decode()
        atual = open(__file__, encoding="utf-8").read()
        if "pra/mim" in novo and novo != atual:
            open(__file__, "w", encoding="utf-8").write(novo)
            print("pra/mim atualizado ✓")
            os.environ["PRAMIM_ATUALIZADO"] = "1"
            exec(compile(novo, __file__, "exec"))
            sys.exit(0)
    except SystemExit:
        raise
    except Exception:
        pass

try:
    import yt_dlp
    from yt_dlp.utils import download_range_func, parse_duration
except ImportError:
    print("yt-dlp não instalado. Rode no a-Shell:  pip install yt-dlp")
    sys.exit(1)

arg = sys.argv[1].strip() if len(sys.argv) > 1 else ""
FMTS = {"mp3": "mp3", "wav": "wav", "4k": "mp4max", "1080": "1080", "mp4": "1080"}
if arg.lower() in FMTS and len(sys.argv) > 2:  # uso manual: pramim.py mp3 [playlist] "link"
    pl = sys.argv[2].lower() == "playlist"
    link = sys.argv[3] if pl and len(sys.argv) > 3 else sys.argv[2]
    arg = base64.urlsafe_b64encode(json.dumps({"u": link, "f": FMTS[arg.lower()], "p": pl}).encode()).decode()
try:
    pedido = json.loads(base64.urlsafe_b64decode(arg + "=" * (-len(arg) % 4)).decode())
except Exception:
    pedido = {"u": arg, "f": "1080"}

url = str(pedido.get("u", "")).strip()
fmt = pedido.get("f", "mp3")
ini, fim = pedido.get("s", ""), pedido.get("e", "")
playlist = bool(pedido.get("p"))

if not re.match(r"^https?://[^\s'\"`<>]+$", url):
    print("Link inválido.")
    sys.exit(1)

# Só o vídeo do link: remove playlist/mix do YouTube
from urllib.parse import urlparse, parse_qs, urlencode
pu = urlparse(url)
if "youtu" in pu.netloc and not playlist:
    q = parse_qs(pu.query)
    if "v" in q:
        url = "https://www.youtube.com/watch?" + urlencode({"v": q["v"][0]})
    elif "youtu.be" in pu.netloc:
        url = "https://youtu.be" + pu.path

pasta = os.path.expanduser("~/Documents/pramim")
os.makedirs(pasta, exist_ok=True)

if playlist:
    opts = {"outtmpl": os.path.join(pasta, "%(playlist_title|Playlist).60s", "%(playlist_index|0)03d - %(title).80s.%(ext)s"),
            "noplaylist": False, "ignoreerrors": True}
else:
    opts = {"outtmpl": os.path.join(pasta, "%(title).80s.%(ext)s"), "noplaylist": True, "playlist_items": "1"}
if fmt in ("mp3", "wav"):
    pp = {"key": "FFmpegExtractAudio", "preferredcodec": fmt}
    if fmt == "mp3":
        pp["preferredquality"] = "0"
    opts.update(format="ba/b", postprocessors=[pp])
elif fmt == "mp4max":
    opts.update(format="bv*+ba/b", merge_output_format="mp4", format_sort=["res", "vcodec:h264"])
else:  # 1080p: prefere H.264 (abre no iPhone); senão o melhor até 1080
    opts.update(format="bv*[vcodec^=avc][height<=1080]+ba/b[vcodec^=avc][height<=1080]/bv*[height<=1080]+ba/b",
                merge_output_format="mp4", format_sort=["vcodec:h264", "res", "acodec:m4a"])

if ini or fim:
    a = parse_duration(ini) or 0
    b = parse_duration(fim) or float("inf")
    opts.update(download_ranges=download_range_func(None, [(a, b)]), force_keyframes_at_cuts=True)

print(f"pra/mim · baixando {fmt.upper()}" + (" · PLAYLIST INTEIRA" if playlist else "") + " …")
with yt_dlp.YoutubeDL(opts) as ydl:
    info = ydl.extract_info(url, download=True)

# Vídeo em VP9/AV1 não abre no iPhone: converte para H.264
if fmt in ("mp4max", "1080") and info and not playlist:
    try:
        dl = (info.get("requested_downloads") or [{}])[0]
        path = dl.get("filepath") or dl.get("_filename")
        vc = (info.get("vcodec") or "") + " " + " ".join(f.get("vcodec") or "" for f in info.get("requested_formats") or [])
        if path and os.path.exists(path) and not re.search(r"avc|h264|hev|hvc", vc):
            print("Convertendo para H.264 (compatível com iPhone)…")
            tmp = path[:-4] + ".ios.mp4"
            import subprocess
            r = subprocess.run(["ffmpeg", "-y", "-i", path, "-c:v", "h264_videotoolbox", "-b:v", "8M",
                                "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", tmp])
            if r.returncode == 0 and os.path.exists(tmp) and os.path.getsize(tmp) > 0:
                os.replace(tmp, path)
            else:
                print("Não deu para converter. Abra o vídeo no VLC.")
    except Exception as e:
        print("Aviso na conversão:", e)
print("✓ Pronto! Arquivos › a-Shell › pramim")
