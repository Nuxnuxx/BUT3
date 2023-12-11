import { Form, Link, useLoaderData } from "react-router-dom";
import FormAjout from "./FormAjout";

function ListDeparts() {
  const { departements } = useLoaderData();

  return (
    <div>
      <h2>Liste des departements</h2>
      <FormAjout />
      {departements.length ? (
        <ul>
          {departements.map((departement) => (
            <li key={departement.code}>
              {departement.nom} : {departement.code}
              <Link to={`/departements/${departement.code}`}>EDITER</Link>
              <Form method="POST" action="destroy">
                <input hidden name="code" value={departement.code} />
                <button>Supprimer</button>
              </Form>
            </li>
          ))}
        </ul>
      ) : (
        <p>Aucun departement</p>
      )}
    </div>
  );
}

export default ListDeparts;
