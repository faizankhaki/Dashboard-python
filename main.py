import streamlit as st
import pandas as pd
import plotly.express as px

# Configure the page
st.set_page_config(page_title="Data Information and Visualization App", layout="wide")

# Title of the app
st.title(" Visualization App")

# File upload
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Read file
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # Creating two columns: left for information, right for plot
    col1, col2 = st.columns([1, 3])

    with col1:
        # Display basic data information
        st.header("Data Information")
        st.write("Number of Rows:", df.shape[0])
        st.write("Number of Columns:", df.shape[1])
        st.write("Number of Empty Rows:", df.isnull().all(axis=1).sum())

        # Display DataFrame
        st.subheader("Data Preview")
        st.write(df.head())

        # Display column names
        st.subheader("Column Names")
        st.write(df.columns.tolist())

    with col2:
        # Plotting section
        st.header("Data Visualization")

        # Select the type of plot
        plot_type = st.selectbox("Select Plot Type", [
            "Scatter Plot", "Line Plot", "Bar Plot", "Histogram", 
            "Box Plot", "Violin Plot", "Pie Chart", "Density Contour"
        ])

        # Select X and Y columns for plotting
        all_columns = df.columns.tolist()
        x_axis = st.selectbox("Select X-axis", all_columns)
        y_axis = st.selectbox("Select Y-axis", all_columns)

        # Select color for the plot
        color_option = st.color_picker("Pick a Color", "#00f900")

        # Advanced customizations
        st.header("Advanced Customizations")
        plot_title = st.text_input("Plot Title", "")
        x_axis_label = st.text_input("X-axis Label", x_axis)
        y_axis_label = st.text_input("Y-axis Label", y_axis)

        # Generate plot based on user selection
        if plot_type == "Scatter Plot":
            fig = px.scatter(df, x=x_axis, y=y_axis, color_discrete_sequence=[color_option])
        elif plot_type == "Line Plot":
            fig = px.line(df, x=x_axis, y=y_axis, color_discrete_sequence=[color_option])
        elif plot_type == "Bar Plot":
            fig = px.bar(df, x=x_axis, y=y_axis, color_discrete_sequence=[color_option])
        elif plot_type == "Histogram":
            fig = px.histogram(df, x=x_axis, color_discrete_sequence=[color_option])
        elif plot_type == "Box Plot":
            fig = px.box(df, x=x_axis, y=y_axis, color_discrete_sequence=[color_option])
        elif plot_type == "Violin Plot":
            fig = px.violin(df, x=x_axis, y=y_axis, color_discrete_sequence=[color_option])
        elif plot_type == "Pie Chart":
            fig = px.pie(df, names=x_axis, values=y_axis, color_discrete_sequence=[color_option])
        elif plot_type == "Density Contour":
            fig = px.density_contour(df, x=x_axis, y=y_axis)

        # Apply advanced customizations
        fig.update_layout(
            title=plot_title,
            xaxis_title=x_axis_label,
            yaxis_title=y_axis_label
        )

        st.plotly_chart(fig, use_container_width=True)
