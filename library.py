import streamlit as st

# Custom CSS for colorful styling
st.markdown(
    """
    <style>
    .book-card {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        background: linear-gradient(135deg, #ff9a9e, #fad0c4);  /* Vibrant gradient background */
    }
    .book-card h3 {
        margin-top: 0;
        color: #333;
    }
    .book-card p {
        margin: 5px 0;
        color: #555;
    }
    .book-card button {
        background-color: #6a11cb;  /* Purple button */
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    .book-card button:hover {
        background-color: #2575fc;  /* Blue hover effect */
    }
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #6a11cb, #2575fc);  /* Modern gradient background */
        padding: 20px;
        border-radius: 10px;
        color: white;
    }
    .sidebar .sidebar-content h2 {
        color: white;
    }
    .sidebar .sidebar-content input, .sidebar .sidebar-content textarea {
        background-color: rgba(255, 255, 255, 0.9);
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 10px;
        margin: 5px 0;
        width: 100%;
    }
    .sidebar .sidebar-content button {
        background-color: #ff9a9e;  /* Pink button */
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        width: 100%;
    }
    .sidebar .sidebar-content button:hover {
        background-color: #fad0c4;  /* Light pink hover effect */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.title("Personal Library Manager")

# Initialize the books list with 4 pre-added books
if 'books' not in st.session_state:
    st.session_state.books = [
        {
            "id": 1,
            "title": "📘 Current Affairs 2023",  # Added book icon
            "author": "Prashant Kumar",
            "year": "2023",
            "description": "A comprehensive guide to the latest national and international events, covering politics, economics, and more.",
            "content": """
            Chapter 1: National Events
            - The government announced new economic policies.
            - Recent elections and their impact.

            Chapter 2: International Events
            - Global climate change summit outcomes.
            - Geopolitical tensions and their implications.
            """,
            "show_content": False  # Toggle for showing/hiding content
        },
        {
            "id": 2,
            "title": "📙 General Knowledge 2023",  # Added book icon
            "author": "Manohar Pandey",
            "year": "2023",
            "description": "An essential book for competitive exams, covering history, geography, science, and current affairs.",
            "content": """
            Chapter 1: History
            - Ancient civilizations.
            - World wars and their consequences.

            Chapter 2: Geography
            - Major rivers and mountains.
            - Climate zones and their characteristics.
            """,
            "show_content": False  # Toggle for showing/hiding content
        },
        {
            "id": 3,
            "title": "📕 English Grammar in Use",  # Added book icon
            "author": "Raymond Murphy",
            "year": "2019",
            "description": "A self-study reference and practice book for intermediate learners of English.",
            "content": """
            Chapter 1: Tenses
            - Present, past, and future tenses.
            - Examples and exercises.

            Chapter 2: Parts of Speech
            - Nouns, verbs, adjectives, etc.
            - Usage in sentences.
            """,
            "show_content": False  # Toggle for showing/hiding content
        },
        {
            "id": 4,
            "title": "📗 A History of Islamic Societies",  # Added book icon
            "author": "Ira M. Lapidus",
            "year": "2014",
            "description": "A detailed and comprehensive history of Islamic civilizations from their origins to the modern era.",
            "content": """
            Chapter 1: Early Islamic History
            - The life of Prophet Muhammad (PBUH).
            - The Rashidun Caliphate.

            Chapter 2: Islamic Golden Age
            - Contributions to science, art, and culture.
            - Major Islamic empires.
            """,
            "show_content": False  # Toggle for showing/hiding content
        }
    ]

# Main section to display and manage books
st.header("Books Library")

# Display all books in a card-like format
if st.session_state.books:
    for book in st.session_state.books:
        st.markdown(
            f"""
            <div class="book-card">
                <h3>{book['title']}</h3>
                <p><strong>Author:</strong> {book['author']}</p>
                <p><strong>Year:</strong> {book['year']}</p>
                <p><strong>Description:</strong> {book['description']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Add a button to toggle book content
        if st.button(f"{'Hide' if book['show_content'] else 'Read'} {book['title']}", key=f"read_{book['id']}"):
            book['show_content'] = not book['show_content']  # Toggle content visibility

        # Display book content if toggled
        if book['show_content']:
            st.subheader(f"Content of {book['title']}")
            st.write(book['content'])
        
        st.write("---")
else:
    st.info("Your library is empty. Add some books!")

# Sidebar for adding a book
with st.sidebar:
    st.header("Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.text_input("Year")
    description = st.text_area("Description")
    content = st.text_area("Content")

    if st.button("Add Book"):
        if title and author and year:
            book = {
                "id": len(st.session_state.books) + 1,
                "title": f"📘 {title}",  # Add book icon to new books
                "author": author,
                "year": year,
                "description": description,
                "content": content,
                "show_content": False  # Default to hidden content
            }
            st.session_state.books.append(book)
            st.success("Book added successfully!")
        else:
            st.error("Please fill in all fields.")

# Remove a book by ID
st.header("Remove a Book")
remove_id = st.number_input("Enter the ID of the book to remove", min_value=1, step=1)

if st.button("Remove Book"):
    if remove_id <= len(st.session_state.books):
        st.session_state.books = [book for book in st.session_state.books if book['id'] != remove_id]
        st.success(f"Book with ID {remove_id} removed successfully!")
    else:
        st.error("Invalid ID. Please enter a valid book ID.")

# Search for a book by title
st.header("Search for a Book")
search_title = st.text_input("Enter the title to search")

if search_title:
    found_books = [book for book in st.session_state.books if search_title.lower() in book['title'].lower()]
    if found_books:
        st.write("Search Results:")
        for book in found_books:
            st.markdown(
                f"""
                <div class="book-card">
                    <h3>{book['title']}</h3>
                    <p><strong>Author:</strong> {book['author']}</p>
                    <p><strong>Year:</strong> {book['year']}</p>
                    <p><strong>Description:</strong> {book['description']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Add a button to toggle book content
            if st.button(f"{'Hide' if book['show_content'] else 'Read'} {book['title']}", key=f"read_{book['id']}"):
                book['show_content'] = not book['show_content']  # Toggle content visibility

            # Display book content if toggled
            if book['show_content']:
                st.subheader(f"Content of {book['title']}")
                st.write(book['content'])
            
            st.write("---")
    else:
        st.warning("No books found with that title.")