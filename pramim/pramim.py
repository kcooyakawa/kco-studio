# pra/mim para iPhone e iPad — roda dentro do a-Shell. powered by KCO Studio
# Uso: python ~/Documents/pramim.py <pedido>
#  <pedido> = base64 (vindo da página pra/mim) ou um link direto (vindo do menu Compartilhar)
import base64, json, os, re, sys

try:
    import yt_dlp
    from yt_dlp.utils import download_range_func, parse_duration
except ImportError:
    print("yt-dlp não instalado. Rode no a-Shell:  pip install yt-dlp")
    sys.exit(1)

arg = sys.argv[1].strip() if len(sys.argv) > 1 else ""
try:
    pedido = json.loads(base64.urlsafe_b64decode(arg + "=" * (-len(arg) % 4)).decode())
except Exception:
    pedido = {"u": arg, "f": "1080"}

url = str(pedido.get("u", "")).strip()
fmt = pedido.get("f", "mp3")
ini, fim = pedido.get("s", ""), pedido.get("e", "")

if not re.match(r"^https?://[^\s'\"`$;|&<>]+$", url):
    print("Link inválido.")
    sys.exit(1)

pasta = os.path.expanduser("~/Documents/pramim")
os.makedirs(pasta, exist_ok=True)

opts = {"outtmpl": os.path.join(pasta, "%(title).80s.%(ext)s"), "noplaylist": True}
if fmt in ("mp3", "wav"):
    pp = {"key": "FFmpegExtractAudio", "preferredcodec": fmt}
    if fmt == "mp3":
        pp["preferredquality"] = "0"
    opts.update(format="ba/b", postprocessors=[pp])
elif fmt == "mp4max":
    opts.update(format="bv*+ba/b", merge_output_format="mp4", format_sort=["res", "vcodec:h264"])
else:  # 1080p, compatível com Fotos/QuickTime
    opts.update(format="bv*[height<=1080]+ba/b[height<=1080]", merge_output_format="mp4",
                format_sort=["vcodec:h264", "res", "acodec:m4a"])

if ini or fim:
    a = parse_duration(ini) or 0
    b = parse_duration(fim) or float("inf")
    opts.update(download_ranges=download_range_func(None, [(a, b)]), force_keyframes_at_cuts=True)

print(f"pra/mim · baixando {fmt.upper()} …")
with yt_dlp.YoutubeDL(opts) as ydl:
    ydl.download([url])
print("✓ Pronto! Arquivos › a-Shell › pramim")
