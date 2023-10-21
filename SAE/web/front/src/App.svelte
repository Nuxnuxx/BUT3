<script>
  import { Route, Router } from 'svelte-routing'
  import Home from './pages/Home.svelte'
  import Auth from './pages/Auth.svelte'
  import Footer from './components/Footer.svelte'
  import Header from './components/Header.svelte'
  import Playlist from './pages/Playlist.svelte'
  import Search from './pages/Search.svelte'
  import Profil from './pages/Profil.svelte'
  import Recipe from './pages/Recipe.svelte'
  import PlaylistCard from './pages/PlaylistCard.svelte'

  import './style.css'

  export let url = ''
</script>

<Router {url}>
  <Header />
  <div>
    <Route path="/" component="{Home}"/>
    <Route path="/auth" component="{Auth}"/>
    <Route path="/playlist" component="{Playlist}"/>
    <Route path="/search" component="{Search}"/>
    <Route path="/profil" component="{Profil}"/>
    <Route path="/playlist/:id" component="{PlaylistCard}"/>
    <Route path="/recipe/:id" component="{Recipe}"/>
  </div>
  <Footer />
</Router>
