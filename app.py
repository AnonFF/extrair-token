import streamlit as st
from urllib.parse import urlparse, parse_qs

st.title("🎮 Extrator de Token Free Fire")
st.write("Cole o link completo abaixo e receba o token pronto para usar.")

link = st.text_area("Cole o link aqui:", height=100, placeholder="https://...")

if st.button("Extrair Token") and link:
    token = None

    # Formato 1: #access_token=...
    if "#" in link:
        fragmento = link.split("#")[1]
        params = parse_qs(fragmento)
        if "access_token" in params:
            token = params["access_token"][0]

    # Formato 2: ?access_token=...
    if not token:
        parsed = urlparse(link)
        params = parse_qs(parsed.query)
        if "access_token" in params:
            token = params["access_token"][0]

    if token:
        st.success("✅ Token extraído com sucesso!")
        st.code(token, language=None)
        st.info("👆 Clique no ícone de copiar no canto do bloco acima.")
    else:
        st.error("❌ Token não encontrado no link. Verifique se o link contém 'access_token='")
