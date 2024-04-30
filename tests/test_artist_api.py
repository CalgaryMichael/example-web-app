def test__get_all_artists(webapp):
    response = webapp.get("/artist/")
    assert response.status_code == 200

    data = sorted(response.get_json(), key=lambda x: x["name"])
    assert len(data) == 3
    assert data[0]["name"] == "John Coltrane"
    assert data[1]["name"] == "Miles Davis"
    assert data[2]["name"] == "Nina Simone"
