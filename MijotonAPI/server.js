const express = require('express');
const app = express();
app.use(express.json());

let recettes = [
    { id: 1, titre: 'recette 1', categorie: 'plat', tempspreparation: 10, imagpath: 'images/image.png' },
    { id: 2, titre: 'recette 2', categorie: 'plat', tempspreparation: 20, imagpath: 'images/image.png' }
];

app.get('/recettes', (req, res) => res.json(recettes));
app.get('/recettes/:id', (req, res) => res.json(recettes.find(r => r.id == req.params.id)));

app.post('/recettes', (req, res) => {
    const nouvelle = { id: recettes.length + 1, ...req.body };
    recettes.push(nouvelle);
    res.status(201).json(nouvelle);
});

app.put('/recettes/:id', (req, res) => {
    const index = recettes.findIndex(r => r.id == req.params.id);
    recettes[index] = { ...recettes[index], ...req.body };
    res.json(recettes[index]);
});

app.delete('/recettes/:id', (req, res) => {
    recettes = recettes.filter(r => r.id != req.params.id);
    res.status(204).send();
});

app.listen(3000, () => console.log('API Express sur http://localhost:3000'));