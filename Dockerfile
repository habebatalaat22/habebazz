FROM python
WORKDIR /app
COPY python.py /app/
COPY paragraphs.txt /app/
RUN pip install nltk
RUN python -m nltk.downloader stopwords punkt
CMD [ "python","python.py" ]