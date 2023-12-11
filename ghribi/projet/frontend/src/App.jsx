import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Accueil from "./components/Accueil";
import Apropos from "./components/Apropos";
import ListDeparts from "./components/ListDeparts";
import {
  action,
  deleteAction,
  loader,
  updateAction,
  updateLoader,
} from "./departement";
import Root from "./Root";
import Departs from "./components/Departs";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    children: [
      { path: "/", element: <Accueil /> },
      { path: "/apropos", element: <Apropos /> },
      {
        path: "/departements",
        element: <ListDeparts />,
        loader: loader,
        action: action,
      },
      {
        path: "/departements/:id",
        element: <Departs />,
        loader: updateLoader,
        action: updateAction,
      },
    ],
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;
