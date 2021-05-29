# my-jame-list-scrap
web scraping for the [MyJameList](http://myjamelist.com/) website
data from the [GiantBomb](giantbomb.com) api
## Endpoints
---
### /seach

#### parameters: 
- query (Required)
- page (Optional)

##### query:
name of the game you want to seach

##### page:
if not specified defaults to 1

##### Example:
GET /seach?query=batman arkham

```json
{
id: 42246,
imagens: {
media: "https://www.giantbomb.com/a/uploads/scale_avatar/8/82063/2560025-baob.jpg",
original: "https://www.giantbomb.com/a/uploads/original/8/82063/2560025-baob.jpg",
pequena: "https://www.giantbomb.com/a/uploads/square_avatar/8/82063/2560025-baob.jpg"
},
nome: "Batman: Arkham Origins Blackgate",
plataformas: "Xbox 360 Games Store;PlayStation Network (PS3);PC;Nintendo 3DS;PlayStation Vita;Nintendo 3DS eShop;Wii U;PlayStation Network (Vita)",
release: "25/10/2013"
}
```

---

### /game

#### parameters
- id

##### id
GiantBomb game id

##### Example:
GET /game?id=42246

```json
{
id: 42246,
imagens: [
"https://www.giantbomb.com/a/uploads/original/46/468536/3210681-red%20son.jpg",
"https://www.giantbomb.com/a/uploads/original/46/468536/3210680-penguin.jpg",
"https://www.giantbomb.com/a/uploads/original/46/468536/3210679-counter%20attack.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050351-4298.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050350-4297.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050349-4296.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050348-4295.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050347-4294.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050346-4293.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050345-4292.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050344-4291.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050343-4290.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050342-4289.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050341-4288.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050340-4287.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050339-4286.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050338-4285.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050337-4284.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050336-4283.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050335-4282.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050334-4281.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050333-4280.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050332-4279.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050331-4264.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050330-4263.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050329-4262.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050328-4261.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050327-4260.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050326-4259.jpg",
"https://www.giantbomb.com/a/uploads/original/27/279909/3050325-4258.jpg"
],
nome: "Batman: Arkham Origins Blackgate",
plataformas: "Xbox 360 Games Store;PlayStation Network (PS3);PC;Nintendo 3DS;PlayStation Vita;Nintendo 3DS eShop;Wii U;PlayStation Network (Vita)",
poster: "https://www.giantbomb.com/a/uploads/original/8/82063/2560025-baob.jpg",
release: "25/10/2013"
}
```

