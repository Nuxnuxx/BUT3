import { Link } from "react-router-dom";

function Nav() {
  return (
    <nav>
      <ul>
        <li>
          <Link to={"/"}> Accueil </Link>
        </li>
        <li>
          <Link to={"/apropos"}> A propos </Link>
        </li>
        <li>
          <Link to={"/departements"}> Departements </Link>
        </li>
      </ul>
    </nav>
  );
}

export default Nav;
