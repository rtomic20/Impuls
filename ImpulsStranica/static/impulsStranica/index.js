const e = React.createElement;

function SearchBar() {
  const [focused, setFocused] = React.useState(false);

  const style = {
    padding: '6px 12px',
    borderRadius: '20px',
    border: '1px solid #ccc',
    width: focused ? '300px' : '250px',
    transition: 'width 0.3s ease'
  };

  return e('input', {
    type: 'text',
    placeholder: 'Pretraži...',
    style,
    onFocus: () => setFocused(true),
    onBlur: () => setFocused(false)
  });
}

const root = ReactDOM.createRoot(document.getElementById('search-root'));
root.render(e(SearchBar));