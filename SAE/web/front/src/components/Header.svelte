<script>
  import { Link } from "svelte-routing"

</script>
<nav>
	<Link to="/">Home</Link>
	<Link to="/auth">Auth</Link>
	<Link to="/playlist">Playlist</Link>
	<Link to="/search">Search</Link>
	<Link to="/profil">Profil</Link>
</nav>


<style>
	nav {
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: center;
		background-color: blue;
	}
</style>
