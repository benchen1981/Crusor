
# scripts/export_chat_pdf.py
# Requires: pip install pdfcrowd
# Usage: python scripts/export_chat_pdf.py --apiuser <user> --apikey <key> --htmlfile conversation.html --outfile conversation.pdf
import argparse
import pdfcrowd
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--apiuser'); parser.add_argument('--apikey'); parser.add_argument('--htmlfile'); parser.add_argument('--outfile')
    args = parser.parse_args()
    client = pdfcrowd.HtmlToPdfClient(args.apiuser, args.apikey)
    with open(args.htmlfile,'rb') as f:
        html = f.read()
    pdf = client.convertHtml(html)
    open(args.outfile,'wb').write(pdf)
if __name__=='__main__':
    main()
