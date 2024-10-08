import './App.css';
import HomePageBodyComponent from './components/HomePageBodyComponent';
import NavBarComponent from './components/NavBarComponent';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import AboutUsComponent from './components/AboutUsComponent';
import InputInfoComponent from './components/InputInfoComponent';

function App() {
  return (
    <div className="App">
      <body className="bg-waves bg-no-repeat bg-center w-full h-full bg-fixed">
        <Router>
          <NavBarComponent />
          <Routes>
            <Route path='/' element={<HomePageBodyComponent />}/>
            <Route path='/aboutus' element={<AboutUsComponent />}/>
            <Route path='/inputinfo' element={<InputInfoComponent />}/>
          </Routes>
        </Router>
      </body>

    </div>
  );
}

export default App;
