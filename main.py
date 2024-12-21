import fitz  # PyMuPDF
from gtts import gTTS


def text_to_audio(text, audio_path):
    tts = gTTS(text=text, lang='en')
    tts.save(audio_path)  # Save the audio to a file

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)  # Open the PDF
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)  # Load each page
        text += page.get_text()  # Extract text from the page
    return text


pdf_path = "input_the_path_to_your_pdf_here/name_if_is_in_same_directory"  # Path to your PDF

# Extract text from PDF
text = extract_text_from_pdf(pdf_path)

text_to_audio(text, "audio.mp3")  # Convert text to audio

print("Text extracted and converted to audio successfully!")