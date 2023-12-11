import { Form } from "react-router-dom";

function FormAjout() {
  return (
    <Form method="POST">
      <input name="nom" placeholder="Nouveau departement" />
      <button> Ajouter Departement</button>
    </Form>
  );
}

export default FormAjout;
