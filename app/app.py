import streamlit as st
import json
from utils import transform_dataframe, load_data


def main():
    st.set_page_config(page_title="Excel2JSON", layout="wide", page_icon="🎲")
    css = """
           <style>
           [data-testid="stSidebar"][aria-expanded="true"]{
               min-width: 350px;
               max-width: 350px;
           }
           """
    st.markdown(css, unsafe_allow_html=True)

    st.title('🎲 Excel2JSON')

    with st.sidebar:
        options = ["特征为列", "特征为行"]
        IsColumn = st.radio(
            "**选择模式**",
            options,
            index=0,
            horizontal=True
        )

        file_uploaded = st.file_uploader("Upload a CSV or Excel file", type=['csv', 'xlsx'])

    # Initialize df as None
    df = None

    if IsColumn == "特征为列":
        if file_uploaded:
            df = load_data(file_uploaded)
    else:
        if file_uploaded:
            df = load_data(file_uploaded)
            df = transform_dataframe(df)

    # Only proceed if df is defined (i.e., a file was successfully uploaded)
    if df is not None:
        # Create two columns for layout
        col1, col2 = st.columns(2)

        with col1:
            # Use Streamlit's data editor for real-time editing on the left
            st.subheader("📊 Excel")
            edited_df = st.data_editor(df, num_rows="dynamic", disabled=False)

        with col2:
            # Convert the edited DataFrame to JSON
            data_dict = edited_df.to_dict(orient='records')
            json_data = json.dumps(data_dict, indent=4, ensure_ascii=False)  # Pretty-printing

            # Display the JSON data on the right
            st.subheader("🎰 JSON")
            st.code(json_data, language='json', line_numbers=True)

        with st.sidebar:
            # Option to download the updated JSON data as a file
            st.download_button(
                label="Download JSON",
                data=json_data,
                file_name="data.json",
                mime="application/json"
            )

    else:
        st.warning("请上传一个文件来继续。")


if __name__ == '__main__':
    main()

    # streamlit run app/app.py
