
# created a context  manually
def global_context(request):
    FAKE_DATABASE = [
        f"https://picsum.photos/id/{id}/1200/600 " for id in range(21, 29)
    ]
    return {
        "fake_database": FAKE_DATABASE,
    }