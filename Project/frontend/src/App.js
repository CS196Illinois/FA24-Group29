import './App.css';
import HomePageBodyComponent from './components/HomePageBodyComponent';
import NavBarComponent from './components/NavBarComponent';

function App() {
  return (
    <div className="App">
      <body className="bg-waves bg-no-repeat bg-center w-full h-full bg-fixed">
        <NavBarComponent />
        <HomePageBodyComponent />
      </body>

    </div>
  );
}

export default App;
