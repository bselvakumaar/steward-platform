
import './styles/theme.css';
import './styles/light.css';

function App() {
  return (
    <div className="app-container">
      <header className="app-header">
        <h1>StockSteward AI</h1>
        <p>Your AI steward for smarter stock ownership.</p>
      </header>
      <main className="app-content">
        <div className="card">
          <h2>Theme Verification</h2>
          <p>If you see a styled card and premium typography, the theme is working.</p>
          <button className="btn-primary">Verify Theme</button>
        </div>
      </main>
    </div>
  );
}

export default App;
