function buttonClick(e, tabName) {
    let tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    e.currentTarget.className += " active";
}

const userpk = document.querySelector('#graph-container').dataset.id
const finished = document.querySelector('#content-container').dataset.id
const likestarset = []
const movieset = []
const starObject = {}
const movieObject = {}
const starArray = document.querySelector('#stararray')
const movieArray = document.querySelector('#moviearray')
axios.get(`/api/v1/accounts/${userpk}/`)
    .then(res => {
        const stars = res.data.likestars
        const movies = res.data.likemovies
        const myStarColor = '#F64F59'
        const neighborColor = '#c471ed'
        const movieColor = '#12c2e9'
        const background = '#eeeeee'
        const edgeColor = '#D3D3D3'
        let graph = {
            nodes: [],
            edges: []
        }
        const db = new sigma.plugins.neighborhoods();

        // add nodes for likestars
        for (let i = 0; i < stars.length; i++) {
            graph.nodes.push({
                id: stars[i].pk,
                label: stars[i].name,
                x: Math.random(),
                y: Math.random(),
                size: 15,
                color: myStarColor
            })
            likestarset.push(stars[i].pk)
            starObject[stars[i].pk] = stars[i].profileimg_set[0]
        }
        // for iteration again to avoid overlapping of starnodes
        for (let i = 0; i < stars.length; i++) {
            if (stars[i].coworker_from) {
                // add nodes for coworker & movies of likestars
                for (let j = 0; j < stars[i].coworker_from.length; j++) {
                    // add nodes for movies of likestars, which is not added
                    const mfound = graph.nodes.some(el => el.id === stars[i].coworker_from[j].movie.pk)
                    if (!mfound) {
                        graph.nodes.push({
                            id: stars[i].coworker_from[j].movie.pk,
                            label: stars[i].coworker_from[j].movie.title,
                            x: Math.random(),
                            y: Math.random(),
                            size: 5,
                            color: movieColor,
                        })
                        movieset.push(stars[i].coworker_from[j].movie.pk)
                        movieObject[stars[i].coworker_from[j].movie.pk] = stars[i].coworker_from[j].movie.poster_set[0]
                    } else {
                        graph.nodes.find(x => x.id === stars[i].coworker_from[j].movie.pk).size = 10
                    }
                    // add nodes for coworker of likestars, who is not added
                    const sfound = graph.nodes.some(el => el.id === stars[i].coworker_from[j].to_star.pk)
                    if (!sfound) {
                        graph.nodes.push({
                            id: stars[i].coworker_from[j].to_star.pk,
                            label: stars[i].coworker_from[j].to_star.name,
                            x: Math.random(),
                            y: Math.random(),
                            size: 7,
                            color: neighborColor
                        })
                        starObject[stars[i].coworker_from[j].to_star.pk] = stars[i].coworker_from[j].to_star.profileimg_set[0]
                    } else {
                        graph.nodes.find(x => x.id === stars[i].coworker_from[j].to_star.pk).size += 2
                    }
                }
            }
        }
        for (let i = 0; i < stars.length; i++) {
            if (stars[i].coworker_from) {
                for (let j = 0; j < stars[i].coworker_from.length; j++) {
                    const efound = graph.edges.some(el => el.id === stars[i].pk + '_' + stars[i].coworker_from[j].movie.pk)
                    // add an edge likestar -> movie
                    if (!efound) {
                        graph.edges.push({
                            id: stars[i].pk + '_' + stars[i].coworker_from[j].movie.pk,
                            source: stars[i].pk,
                            target: stars[i].coworker_from[j].movie.pk,
                            size: 1,
                            color: edgeColor
                        })
                    }
                    // add edges movie -> to_stars
                    const eefound = graph.edges.some(el => el.id === stars[i].coworker_from[j].movie.pk + '_' + stars[i].coworker_from[j].to_star.pk)
                    if (!eefound) {
                        graph.edges.push({
                            id: stars[i].coworker_from[j].movie.pk + '_' + stars[i].coworker_from[j].to_star.pk,
                            source: stars[i].coworker_from[j].movie.pk,
                            target: stars[i].coworker_from[j].to_star.pk,
                            size: 1,
                            color: edgeColor
                        })
                    }
                }
            }
        }
        // sigma.renderers.def = sigma.renderers.canvas
        // Instantiate sigma:
        s = new sigma({
            graph: graph,
            container: 'graph-container',
            type: 'canvas'
        });

        // find all neighborhood
        function dfs(nArray) {
            let nStack = nArray.map(el => el.id)
            let point = 1
            while (point < nStack.length) {
                s.graph.neighborhood(nStack[point]).nodes.forEach(el => {
                    if (!(nStack.includes(el.id))) { nStack.push(el.id) }
                })
                point += 1
            }
            return nStack
        }

        // Initialize the dragNodes plugin:
        let dragListener = sigma.plugins.dragNodes(s, s.renderers[0]);
        dragListener.bind('startdrag', function (event) { });
        dragListener.bind('drag', function (event) { });
        dragListener.bind('drop', function (event) { });
        dragListener.bind('dragend', function (event) { });

        // initialize the neighborhood
        s.bind('clickNode', function (e) {
            document.querySelectorAll('div.defaultarray').forEach(el => el.style.display = "none")
            starArray.innerHTML = ""
            movieArray.innerHTML = ""
            let nodeId = e.data.node.id,
                toKeep = dfs(s.graph.neighborhood(nodeId).nodes);

            s.graph.nodes().forEach(function (n) {
                if (toKeep.includes(n.id)) {
                    let starimg = document.createElement("div")
                    starimg.classList.add("mx-2", "renderingarray")
                    if (likestarset.includes(n.id) & finished.includes(n.id)) {
                        n.color = myStarColor
                        starimg.innerHTML = `<img src="${starObject[n.id]}" class="staravatar card-img">
                        <a href="/stars/${n.id}"><button class="btn btn-sm w-100"
                        style="background-image: linear-gradient(to right, #12c2e9, #c471ed, #f64f59)">
                        ${n.label}
                      </button>`
                    } else if (likestarset.includes(n.id)) {
                        n.color = myStarColor
                        starimg.innerHTML = `<img src="${starObject[n.id]}" class="staravatar card-img">
                        <a href="/stars/${n.id}"><button class="btn btn-sm w-100 mypurple">
                        ${n.label}
                      </button>`
                    } else if (!movieset.includes(n.id)) {
                        n.color = neighborColor
                        starimg.innerHTML = `<img src="${starObject[n.id]}" class="staravatar card-img">
                        <a href="/stars/${n.id}"><button class="btn btn-sm w-100 btn-default">
                        ${n.label}
                      </button>`
                    } else {
                        n.color = movieColor
                        let movieimg = document.createElement("div")
                        movieimg.classList.add("mx-2", "renderingarray")
                        if (movies.includes(n.id)) {
                            movieimg.innerHTML = `<a href="{% url 'movies:detail' movie.pk %}">
                            <img src="${movieObject[n.id]}" alt="Card image" class="movieposter"></a>`
                        } else {
                            movieimg.innerHTML = `<a href="{% url 'movies:detail' movie.pk %}">
                            <img src="${movieObject[n.id]}" alt="Card image" class="movieposter" style="-webkit-filter: grayscale(100%);
                            filter: grayscale(100%);"></a>`
                        }

                        movieArray.appendChild(movieimg)
                    }
                    starArray.appendChild(starimg)
                } else {
                    n.color = '#eee'
                }
            });

            s.graph.edges().forEach(function (e) {
                if ((toKeep.includes(e.source)) && (toKeep.includes(e.target))) {
                    e.color = edgeColor
                } else {
                    e.color = background
                }
            });

            s.refresh()
        })
        s.bind('clickStage', function (e) {
            starArray.innerHTML = ""
            movieArray.innerHTML = ""
            document.querySelectorAll('div.defaultarray').forEach(el => el.style.display = "flex")
            s.graph.nodes().forEach(function (n) {
                if (likestarset.includes(n.id)) {
                    n.color = myStarColor
                } else if (movieset.includes(n.id)) {
                    n.color = movieColor
                } else {
                    n.color = neighborColor
                }
            });
            s.graph.edges().forEach(function (e) {
                e.color = edgeColor;
            });
            s.refresh();
        });
    })
