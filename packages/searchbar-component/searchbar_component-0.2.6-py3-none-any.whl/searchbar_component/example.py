import streamlit as st
from searchbar_component import searchbar
import requests

def search_wikipedia(query):
    if not query:
        return []

    response = requests.get(
        "https://en.wikipedia.org/w/api.php",
        params={
            "action": "opensearch",
            "format": "json",
            "search": query,
            "limit": 10
        }
    ).json()

    # Simulating Elasticsearch highlight feature with more flexible bolding
    titles = response[1]
    highlighted_titles = []
    for title in titles:
        # Example: Let's assume we want to bold the matched query within the title
        # This is a simplification and should be adjusted based on actual highlight data structure
        bolded_title = title.replace(query, f"<b>{query}</b>")
        highlighted_titles.append({"label": title, "value": title, "bold": bolded_title})

    return highlighted_titles

def perform_search(query):
    st.write(f"Searching for: {query}")
    search_results = search_wikipedia(query)
    st.write("Search results:", search_results)
    return search_results

st.title("Wikipedia Search using Searchbar Component")
st.write("This example demonstrates how to use the searchbar component with custom styling and bold text in suggestions.")

# Initialize session state
if 'suggestions' not in st.session_state:
    st.session_state.suggestions = []
if 'last_query' not in st.session_state:
    st.session_state.last_query = ""
if 'last_search' not in st.session_state:
    st.session_state.last_search = ""

# Custom style overrides
style_overrides = {
    "clear": {
        "width": 20,
        "height": 20,
        "fill": "#aaa"
    },
    "plus": {
        "width": 18,
        "height": 18,
        "fill": "#aaa"
    },
    "input": {
        "backgroundColor": "#f0f0f0",
        "color": "#333"
    },
    "suggestion": {
        "backgroundColor": "#fff",
        "color": "#333",
        "hoverBackgroundColor": "#e0e0e0",
        "hoverColor": "#000"
    }
}

# Use the searchbar component with custom styling and bold text
result = searchbar(
    key="wiki_search",
    placeholder="Search Wikipedia",
    suggestions=st.session_state.suggestions,
    highlightBehavior="keep",  # Options: "keep", "update", "partial"
    style_overrides=style_overrides
)

# Handle the result from the searchbar
if result:
    if result.get("interaction") == "search":
        query = result["value"]
        if query != st.session_state.last_query and query != st.session_state.last_search:
            st.session_state.last_query = query
            st.session_state.suggestions = search_wikipedia(query)
            st.experimental_rerun()
    elif result.get("interaction") == "submit":
        query = result["value"]
        perform_search(query)
        st.session_state.last_search = query
        st.session_state.suggestions = []
    elif result.get("interaction") == "select":
        selected = result["value"]
        st.write(f"You selected: {selected['label']}")
        st.session_state.last_search = selected['label']
        st.session_state.suggestions = []
    elif result.get("interaction") == "reset":
        st.session_state.suggestions = []
        st.session_state.last_query = ""
        st.session_state.last_search = ""
    elif result.get("interaction") == "plus_click":
        clicked_suggestion = result["value"]
        st.write(f"You clicked the plus button for: {clicked_suggestion['label']}")
        # Add your custom logic here for handling the plus button click

st.write("Try typing a search term in the box above to see autocomplete suggestions with custom styling and bold text.")
st.write("You can use arrow keys to navigate suggestions and Enter to select.")
st.write("Notice the plus icon that appears on the right side of the highlighted suggestion.")
