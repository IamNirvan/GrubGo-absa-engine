@echo off

echo Installing dependencies...
pip install "setfit[absa]"
pip install transformers==4.39.0

echo Checking if spaCy models are installed...
python -c "import spacy; exit(0 if spacy.util.is_package('en_core_web_lg') else 1);" 
if errorlevel 1 (
    echo Downloading en_core_web_lg...
    spacy download en_core_web_lg
)
echo en_core_web_lg is already installed

python -c "import spacy; exit(0 if spacy.util.is_package('en_core_web_sm') else 1);"
if errorlevel 1 (
    echo Downloading en_core_web_sm...
    spacy download en_core_web_sm
)
echo en_core_web_sm is already installed

echo Dependencies installed