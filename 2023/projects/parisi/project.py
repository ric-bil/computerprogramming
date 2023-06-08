import streamlit as st
import stanza
from googletrans import Translator

translator = Translator()
upos_dict = {
    'ADJ': 'Adjective',
    'ADP': 'Adposition',
    'ADV': 'Adverb',
    'AUX': 'Auxiliary verb',
    'CCONJ': 'Coordinating conjunction',
    'DET': 'Determiner',
    'INTJ': 'Interjection',
    'NOUN': 'Noun',
    'NUM': 'Numeral',
    'PART': 'Particle',
    'PRON': 'Pronoun',
    'PROPN': 'Proper noun',
    'PUNCT': 'Punctuation',
    'SCONJ': 'Subordinating conjunction',
    'SYM': 'Symbol',
    'VERB': 'Verb',
    'X': 'Other'
}
@st.cache(suppress_st_warning=True)
def translate_text(input_text, dest_lang):
    try:
        output_dict = translator.translate(input_text, dest=dest_lang)
        translated_text = output_dict.text
        return translated_text
    except ValueError:
        st.warning(f"{dest_lang} is not a valid language!")
        return None

@st.cache(suppress_st_warning=True)
def analyze_text(translated_text, dest_lang):
    try:
        stanza.download(dest_lang)
        lan_nlp = stanza.Pipeline(dest_lang, processors="tokenize, mwt, lemma, pos")
        text = lan_nlp(translated_text)
        return text
    except stanza.pipeline.core.UnsupportedProcessorError:
        st.info("Sorry, text in this language cannot be analyzed.")
        return None
    except stanza.resources.common.UnknownLanguageError:
        st.warning("This language code is unknown! Try typing the language name in full characters.")
        return None

def main():
    if 'clicked' not in st.session_state:
        st.session_state['clicked'] = 0

    st.title('Super Translaton 3000')
    st.header('Welcome to the improved version of Super Translaton 3000! This app is based on the previous one, except some improvements on caching.')
    st.write('''This app allows you to translate and then analyze a text in any language,
    as long as Stanza and Google Translate support it. To use it, just type a text in any language of your
    choice. It will be automatically recognized. Then, choose a language. You can write the
    name of the language in English or just type the two-letter code (e.g., for Spanish, you
    can either type "Spanish" or "es"). You will have a translation and then you can
    walk through the sentences of the translated text. When selecting a sentence,
    you will have clickable single tokens. When clicking them, you will get the lemma and the part
    of speech of the desired word.''')

    input_text = st.text_area('Please, insert text here')
    dest_lang = st.text_input('Enter a language here')

    st.subheader("Translation")
    if input_text and dest_lang:
        with st.spinner("Translating..."):
            translated_text = translate_text(input_text, dest_lang)
        if translated_text:
            st.write(translated_text)

    st.subheader("Analyzer")
    if input_text and dest_lang:
        with st.spinner("Analyzing..."):
            analyzed_text = analyze_text(translated_text, dest_lang)
        if analyzed_text:
            for i, sent in enumerate(analyzed_text.sentences):
                sentence_text = sent.text
                if st.button(f"Sentence {i+1}: {sentence_text}", key=f"sentence_{i+1}"):
                    st.session_state['clicked'] = i + 1
                if st.session_state['clicked'] == i + 1:
                    st.subheader(f"Sentence {i+1}:")
                    for x, word in enumerate(sent.words):
                        if word.pos == 'PUNCT':
                            continue
                        word_text = str(word.text)
                        if st.button(word_text, key=f"word_{i}_{x}"):
                            lemma = word.lemma
                            upos = word.upos
                            feats = word.feats
                            upos_label = upos_dict.get(upos, 'Unknown')
                            st.info(f"**Lemma**: {lemma}; **Part of Speech**: {upos_label}, **Features**: {feats}")
                        else:
                            pass

if __name__ == "__main__":
    main()
