mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
heaadless = true\n\
\n\
" > ~/.streamlit/config.toml