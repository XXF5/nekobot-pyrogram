import argparse
import sys
import os

def get_args():
    parser = argparse.ArgumentParser(description="Inicializa el bot con credenciales")

    parser.add_argument("-a", "--api_id", default=os.getenv("API_ID"), help="API ID de Telegram")
    parser.add_argument("-H", "--api_hash", default=os.getenv("API_HASH"), help="API Hash de Telegram")
    parser.add_argument("-t", "--bot_token", default=os.getenv("TOKEN"), help="Token del bot")
    parser.add_argument("-ss", "--session_string", default=os.getenv("SESSION_STRING"), help="Session string del usuario")
    parser.add_argument("-id", default=os.getenv("USER_ID"), help="ID personalizado requerido si se usa -ss")
    parser.add_argument("-b", "--barer", default=os.getenv("GIT_API"), help="Token de autenticación Bearer")
    parser.add_argument("-r", "--repo", default=os.getenv("GIT_REPO"), help="Repositorio o URL del repositorio")
    parser.add_argument("-owner", default=os.getenv("OWNER"), help="Owner o propietario (opcional)")
    parser.add_argument("-w", "--web", default=os.getenv("WEB_LINK"), help="URL web opcional")

    args = parser.parse_args()

    # تحقق أساسي
    if not args.api_id or not args.api_hash:
        sys.exit("API_ID و API_HASH مطلوبين")

    if args.bot_token and args.session_string:
        sys.exit("لا يمكن استخدام bot_token و session_string معًا")

    if not args.bot_token and not args.session_string:
        sys.exit("يجب توفير TOKEN أو SESSION_STRING")

    if args.session_string and not args.id:
        sys.exit("إذا استخدمت SESSION_STRING يجب توفير USER_ID")

    if not args.barer or not args.repo:
        sys.exit("GIT_API و GIT_REPO مطلوبين")

    return args
