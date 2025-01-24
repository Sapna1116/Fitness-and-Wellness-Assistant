import streamlit as st
from api_utils import upload_document, list_documents, delete_document

def display_sidebar():
    # Model selection
    model_options = ["gpt-4o", "gpt-4o-mini"]
    st.sidebar.selectbox("Select Model", options=model_options, key="model")

    # Document upload
    st.sidebar.header("Upload Document")
    uploaded_file = st.sidebar.file_uploader("Choose a file", type=["pdf", "docx", "html"])
    if uploaded_file and st.sidebar.button("Upload"):
        with st.spinner("Uploading..."):
            print(f"st.session_state : {st.session_state}")
            upload_response = upload_document(uploaded_file)
            if upload_response:
                st.sidebar.success(f"File  '{uploaded_file.name}' uploaded successfully with ID {upload_response['file_id']}.")
                st.session_state.documents = list_documents()

    # List documents
    st.sidebar.header("Uploaded Documents")
    if st.sidebar.button("Refresh Document List"):
        with st.spinner("Refreshing..."):
            st.session_state.documents = list_documents()

    # Initialize document list if not present
    if "documents" not in st.session_state:
        st.session_state.documents = list_documents()
        
    # Display document list and delete functionality
    if "documents" in st.session_state and st.session_state.documents:
        for doc in st.session_state.documents:
            st.sidebar.text(f"{doc['filename']} (ID: {doc['id']}), Uploaded: {doc['upload_timestamp']})")

        # Delete Document
        selected_file_id = st.sidebar.selectbox("Select a document to delete", 
                                                options=[doc['id'] for doc in st.session_state.documents], format_func=lambda x: next(doc['filename'] for doc in st.session_state.documents if doc['id'] == x))
        if st.sidebar.button("Delete Selected Document"):
            with st.spinner("Deleting..."):
                delete_response = delete_document(selected_file_id)
                if delete_response:
                    st.sidebar.success(f"Document with ID {selected_file_id}  deleted successfully.")
                    st.session_state.documents = list_documents()  # Refresh the list after deletion
                else:
                    st.sidebar.error(f"Failed to delete document with ID {selected_file_id}.")
