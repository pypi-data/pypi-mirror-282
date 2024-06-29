import streamlit as st
from searchbar_component import searchbar

def get_suggestions(query):
    # Simulating some search results with bold parts
    suggestions = [
        {"label": "Apple", "value": "apple", "bold": "<b>App</b>le"},
        {"label": "Banana", "value": "banana", "bold": "Bana<b>na</b>"},
        {"label": "Cherry", "value": "cherry", "bold": "Che<b>rry</b>"},
        {"label": "Date", "value": "date", "bold": "Da<b>te</b>"},
        {"label": "Elderberry", "value": "elderberry", "bold": "Eld<b>erberry</b>"},
    ]
    return [s for s in suggestions if query.lower() in s["value"]]

st.title("Searchbar with Bold Text Example")

# Initial suggestions
suggestions = get_suggestions("")

# Use the searchbar component with bold text feature
result = searchbar(
    key="bold_searchbar",
    placeholder="Type to search",
    suggestions=suggestions,
    highlightBehavior="keep",  # Options: "keep", "update", "partial"
    style_overrides={
        "clear": {"fill": "#ff0000"},
        "plus": {"fill": "#00ff00"},
    }
)

# Handle the result from the searchbar
if result:
    if result.get("interaction") == "search":
        query = result["value"]
        st.session_state.suggestions = get_suggestions(query)
        st.experimental_rerun()
    elif result.get("interaction") == "select":
        selected = result["value"]
        st.write(f"You selected: {selected['label']}")
    elif result.get("interaction") == "submit":
        query = result["value"]
        st.write(f"You submitted: {query}")
    elif result.get("interaction") == "plus_click":
        clicked_suggestion = result["value"]
        st.write(f"You clicked the plus button for: {clicked_suggestion['label']}")
    elif result.get("interaction") == "reset":
        st.write("Search has been reset")

st.write("Try typing a search term in the box above to see autocomplete suggestions with bold text.")
