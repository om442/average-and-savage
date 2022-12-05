import ReactDOM from "react-dom";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./page/Layout";
import Home from "./page/Home";
import About from "./page/About";
import NoPage from "./page/NoPage";
import Projects from "./page/Projects";
import Recommendation from "./page/Recommendation";

import 'bootstrap/dist/css/bootstrap.css';
import "./index.css";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="about" element={<About />} />
          <Route path="projects" element={<Projects />} />
          <Route path="recommendation" element={<Recommendation />} />
          <Route path="*" element={<NoPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));