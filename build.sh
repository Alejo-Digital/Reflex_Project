pip install --upgrade pip
pip install --upgrade reflex
pip install -r requirements.txt
reflex init
reflex export --frontend-only
rm -rf public
unzip frontend.zip -d public
rm -f frontend.zip