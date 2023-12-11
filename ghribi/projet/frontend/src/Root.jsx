import Nav from "./components/Nav";
import { Outlet } from "react-router-dom";

function Root() {
  return (
    <>
      <Nav />
      <Outlet />
    </>
  );
}

export default Root;
