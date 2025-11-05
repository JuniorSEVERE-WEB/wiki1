# Django Wiki Encyclopedia 📚

A full-featured Wikipedia-style encyclopedia web application built with Django. This project allows users to browse, search, create, and edit encyclopedia entries with a clean, user-friendly interface.

##  Features

###  Core Functionality
- **Browse Encyclopedia Entries**: View all available encyclopedia entries from the homepage
- **Entry Pages**: Read individual encyclopedia entries with proper Markdown rendering
- **Search Functionality**: 
  - Exact match search redirects directly to the entry
  - Substring search displays a list of matching entries
- **Create New Entries**: Add new encyclopedia entries with Markdown support
- **Edit Existing Entries**: Modify existing entries with pre-populated content
- **Random Page**: Discover random encyclopedia entries

###  User Interface
- **Responsive Design**: Clean, Wikipedia-inspired interface
- **Sidebar Navigation**: Easy access to all features
- **Error Handling**: Custom 404-style pages for non-existent entries
- **Enhanced Edit Button**: Prominently positioned for better visibility

###  Technical Features
- **Custom Markdown Parser**: Built-in regex-based Markdown to HTML conversion
  - Headers (H1-H6)
  - Bold and italic text
  - Links with proper HTML output
  - Unordered lists
  - Inline code blocks
  - Automatic paragraph detection
- **No External Dependencies**: Custom Markdown parser eliminates need for external libraries
- **Django Best Practices**: Proper MVC architecture, template inheritance, and form handling

##  Getting Started

### Prerequisites
- Python 3.8 or higher
- Django 5.2.7 or higher

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/JuniorSEVERE-WEB/wiki1.git
   cd wiki1
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # macOS/Linux
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run the development server**
   ```bash
   python manage.py runserver
   ```

5. **Open your browser**
   Navigate to `http://127.0.0.1:8000/` to start using the wiki!

## 📁 Project Structure

```
wiki/
├── encyclopedia/           # Main application
│   ├── static/
│   │   └── encyclopedia/
│   │       └── styles.css  # Custom styling
│   ├── templates/
│   │   └── encyclopedia/   # HTML templates
│   ├── templatetags/       # Custom template filters
│   ├── views.py           # Application logic
│   ├── urls.py            # URL routing
│   └── util.py            # Utility functions
├── entries/               # Encyclopedia entries (Markdown files)
├── wiki/                 # Django project settings
└── manage.py            # Django management script
```

##  Usage

### Browsing Entries
- Visit the homepage to see all available encyclopedia entries
- Click on any entry title to read the full article

### Searching
- Use the search box in the sidebar
- Exact matches redirect directly to the entry
- Partial matches show a list of suggestions

### Creating New Entries
- Click "Create New Page" in the sidebar
- Enter a title and content in Markdown format
- Validation prevents duplicate entries

### Editing Entries
- Click the "Edit" button on any entry page
- Modify the content using Markdown syntax
- Save changes to update the entry

### Random Discovery
- Click "Random Page" in the sidebar to discover random entries

##  Markdown Support

The wiki supports the following Markdown syntax:

```markdown
# Headers (H1-H6)
## Subheaders
### And so on...

**Bold text** or __Bold text__
*Italic text* or _Italic text_

[Link text](https://example.com)

- Unordered list item
- Another item

`Inline code`
```

## 🛠️ Development

### Key Files
- `encyclopedia/views.py`: Contains all the view logic (index, search, create, edit, random)
- `encyclopedia/templates/`: HTML templates with Django template inheritance
- `encyclopedia/templatetags/markdown_extras.py`: Custom Markdown parser
- `encyclopedia/urls.py`: URL routing configuration

### Custom Features
- **Regex-based Markdown Parser**: No external dependencies required
- **Smart Search**: Handles both exact and substring matching
- **Form Validation**: Prevents duplicate entries and validates input
- **Error Handling**: User-friendly error pages

##  Sample Entries

The wiki comes pre-loaded with sample entries:
- **CSS**: Cascading Style Sheets information
- **Django**: Python web framework details  
- **Git**: Version control system guide
- **HTML**: HyperText Markup Language reference
- **Python**: Programming language overview

##  Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

##  License

This project is open source and available under the [MIT License](LICENSE).

##  Future Enhancements

- [ ] User authentication system
- [ ] Entry revision history
- [ ] Image upload support
- [ ] Advanced search filters
- [ ] Entry categories and tags
- [ ] Export entries to PDF
- [ ] Mobile app version

##  Author

**JuniorSEVERE-WEB**
- GitHub: [@JuniorSEVERE-WEB](https://github.com/JuniorSEVERE-WEB)

##  Acknowledgments

- Built as part of CS50's Web Programming with Python and JavaScript course
- Inspired by Wikipedia's clean and functional design
- Django framework for robust web development capabilities

---

 **Star this repository if you found it helpful!**