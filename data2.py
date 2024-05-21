import streamlit as st
import pandas as pd
import plotly.express as px

# Function to load dataset
def load_data(file):
    data = pd.read_csv(file)
    return data

# Function to preprocess data (remove null values and delete selected columns)
def preprocess_data(data, preprocess_flag, selected_columns):
    if preprocess_flag:
        st.subheader("Data Before Preprocessing")
        st.write(data)
        st.write("Number of Rows Before Preprocessing:", len(data))
        
        # Remove null values
        data.dropna(inplace=True)
        
        # Delete selected columns
        data.drop(columns=selected_columns, inplace=True)
        
        st.subheader("Data After Preprocessing")
        st.write(data)
        st.write("Number of Rows After Preprocessing:", len(data))
    else:
        st.subheader("Data Without Preprocessing")
        st.write(data)
        st.write("Number of Rows:", len(data))
    return data

# Function to plot line plot
def plot_line_plot(data, x_column, y_column):
    fig = px.line(data, x=x_column, y=y_column, title="Line Plot")
    st.plotly_chart(fig, use_container_width=True)

# Function to plot scatter plot
def plot_scatter_plot(data, x_column, y_column):
    fig = px.scatter(data, x=x_column, y=y_column, title="Scatter Plot")
    st.plotly_chart(fig, use_container_width=True)

# Function to plot bar plot
def plot_bar_plot(data, x_column, y_column):
    fig = px.bar(data, x=x_column, y=y_column, title="Bar Plot")
    st.plotly_chart(fig, use_container_width=True)

# Function to plot histogram
def plot_histogram(data, x_column):
    fig = px.histogram(data, x=x_column, title="Histogram")
    st.plotly_chart(fig, use_container_width=True)

# Function to plot pie chart
def plot_pie_chart(data, x_column):
    fig = px.pie(data, names=x_column, title="Pie Chart")
    st.plotly_chart(fig, use_container_width=True)

# Function to plot box plot
def plot_box_plot(data, y_column):
    fig = px.box(data, y=y_column, title="Box Plot")
    st.plotly_chart(fig, use_container_width=True)

# Function to plot violin plot
def plot_violin_plot(data, y_column):
    fig = px.violin(data, y=y_column, title="Violin Plot")
    st.plotly_chart(fig, use_container_width=True)

# Function to plot heat map
def plot_heat_map(data):
    numeric_data = data.select_dtypes(include=['float', 'int'])
    fig = px.imshow(numeric_data.corr(), title="Correlation Heatmap")
    st.plotly_chart(fig, use_container_width=True)

# Function to plot bubble chart
def plot_bubble_chart(data, x_column, y_column):
    fig = px.scatter(data, x=x_column, y=y_column, size=y_column, title="Bubble Chart")
    st.plotly_chart(fig, use_container_width=True)

# Function to plot area plot
def plot_area_plot(data, x_column, y_column):
    fig = px.area(data, x=x_column, y=y_column, title="Area Plot")
    st.plotly_chart(fig, use_container_width=True)

def main():
    st.set_page_config(page_title="Plotly Explorer: Visualize Diverse Datasets", page_icon="📊", layout="wide")
    st.title("Plotly Explorer: Visualize Diverse Datasets")

    # Add background pattern
    st.markdown(
        """
        <style>
        body {
            background: #E0E0E0;
        }
        
        .reportview-container {
            background: linear-gradient(to right, #BDBDBD, #E0E0E0);
            position: relative;
            overflow: hidden;
        }

        .shape {
            width: 150px;
            height: 150px;
            position: absolute;
            border-radius: 50%;
            background-color: rgba(255, 255, 255, 0.1);
        }

        .shape1 {
            top: 0;
            left: 0;
            transform: rotate(45deg);
        }

        .shape2 {
            top: 50%;
            right: 0;
            transform: rotate(135deg);
        }

        .shape3 {
            bottom: 0;
            left: 50%;
            transform: rotate(225deg);
        }

        .shape4 {
            bottom: 50%;
            right: 50%;
            transform: rotate(315deg);
        }

        h1, h2, h3, h4, h5, h6 {
            color: #800000; /* Maroon color */
        }
        </style>
        """
        , unsafe_allow_html=True
    )

    # Upload dataset
    st.sidebar.title("Upload Dataset")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        data = load_data(uploaded_file)

        # Select columns for preprocessing
        preprocess_flag = st.sidebar.checkbox("Preprocess Dataset")
        selected_columns = []
        if preprocess_flag:
            st.sidebar.subheader("Select Columns to Delete")
            selected_columns = st.sidebar.multiselect("Columns", data.columns)

        # Preprocess data
        data = preprocess_data(data, preprocess_flag, selected_columns)

        # Select plot type
        plot_type = st.sidebar.selectbox("Select Plot Type", 
                                          ["Line Plot", "Scatter Plot", "Bar Plot", "Histogram", 
                                           "Pie Chart", "Box Plot", "Violin Plot", "Heat Map", 
                                           "Bubble Chart", "Area Plot"])

        if plot_type == "Histogram":
            x_column_hist = st.sidebar.selectbox("Select X-axis for Histogram", data.columns)
            plot_histogram(data, x_column_hist)
        elif plot_type == "Heat Map":
            plot_heat_map(data)
        else:
            x_column = st.sidebar.selectbox("Select X-axis", data.select_dtypes(include=['number']).columns)
            y_column = st.sidebar.selectbox("Select Y-axis", data.select_dtypes(include=['number']).columns)
            
            if plot_type == "Line Plot":
                plot_line_plot(data, x_column, y_column)
            elif plot_type == "Scatter Plot":
                plot_scatter_plot(data, x_column, y_column)
            elif plot_type == "Bar Plot":
                plot_bar_plot(data, x_column, y_column)
            elif plot_type == "Pie Chart":
                plot_pie_chart(data, x_column)
            elif plot_type == "Box Plot":
                plot_box_plot(data, y_column)
            elif plot_type == "Violin Plot":
                plot_violin_plot(data, y_column)
            elif plot_type == "Bubble Chart":
                plot_bubble_chart(data, x_column, y_column)
            elif plot_type == "Area Plot":
                plot_area_plot(data, x_column, y_column)

if __name__ == "__main__":
    main()
