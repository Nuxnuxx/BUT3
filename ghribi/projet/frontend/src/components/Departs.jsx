import { Form, useLoaderData } from "react-router-dom";

function Departs() {
  const { departement } = useLoaderData();

  return (
    <div>
      <Form method="POST">
        <input name="nom" placeholder="Nouveau nom" />
        <button> Modifier Departement</button>
      </Form>
      {departement.nom} : {departement.code}
    </div>
  );
}

export default Departs;
