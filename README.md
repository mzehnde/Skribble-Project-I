# PDFMail_Heroku

This project serves as an example of an endpoint used for the callback functionality of Skribbles API regarding a succesfully signed PDF file.
The application has been deployed to Heroku such that the endpoint can be called. We provide the URL of this endpoint in the following example as a callback_success_url
> https://github.com/BlockSigner/api-examples/tree/main/Python/Upload_Download_PDFs

## How does it work
Once the document has been succesfully signed a POST request to this endpoint is automatically called. In this request the API of Skribble is used to receive the content of the signed file.
We use the following API call to do that:
> https://api.scribital.com/v1/documents/'SKRIBBLE_DOCUMENT_ID/content

After that we use MIME to send an Email to the adress that has been provided as an argument. The signed file will be attached to it as a PDF. 




