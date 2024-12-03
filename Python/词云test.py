import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text
def segment_text(text):
    return " ".join(jieba.cut(text))
def generate_wordcloud(text):
    mask = np.array(Image.open('images.jpg'))
    print(mask.shape)
    wordcloud = WordCloud(mask=mask,font_path="msyh.ttc",background_color="white",width=2500,height=3000).generate(text)
    plt.figure(figsize=(10, 8))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
def main():
    file_path = "gov_report.txt"
    text = load_text(file_path)
    segmented_text = segment_text(text)
    generate_wordcloud(segmented_text)
if __name__ == "__main__":
    main()
