const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(React.createElement(ImpulsOverview));
function ImpulsOverview() {
    return (
        React.createElement('div', { className: 'container' },

            React.createElement('a', {
                href: '/',
                className: 'back-home'
            }, '⬅️ Povratak na početnu 🏠'),

           
            React.createElement('h1', null, 'Dobrodošli u Impuls upute'),

            
            React.createElement('p', null,
                'Ovdje možete pronaći sažete upute za referenciranje, navođenje literature te tablica i slika prema najnovijim APA standardima (7. izdanje). Ako vam je potreban detaljan vodič, preuzmite dokument klikom na gumb ispod.'
            ),

            React.createElement('a', {
                href: '/download/',
                className: 'download-button'
            }, '📥 Preuzmi APA upute'),

            React.createElement('div', { className: 'footer' },
                '📚 Pripremljeno s ljubavlju za Impuls tim ❤️'
            )
        )
    );
}

