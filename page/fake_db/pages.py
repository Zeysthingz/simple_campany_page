#   Create fake database for pages with doc strings
CONTACT_DETAILS='''
            <div class="container">
                <div class="row">
                    <!--            sağ ve soldan 2lk grıdler bos kalır offset ıkı olmasıda sagdan ıkı bosluk yana kaydırması demektır-->
                    <div class="col-sm-8 offset-2 mb-5">
                        <h2>Adress</h2>
                        <adress>
                            <p>Zeysthingz Company 1234 Main St Springfield, MA 12345 Turkey</p>
                        </adress>
                        <hr>
                        <!--                burda form ekleyeceğim-->
                        <h2 class="mt-5">Have a question? Send us a message!</h2>
                        <form class="row g-3">
                            <div class="col-12">
                                <label for="inputEmail4" class="form-label">Email</label>
                                <input type="email" class="form-control" id="inputEmail4">
                            </div>
                            <div class="col-12">
                                <label for="explanation">Explanation</label>
                                <textarea class="form-control" placeholder="Leave a comment here" id="explanation"
                                          style="height: 100px"></textarea>
                            </div>
                            <div class="col-12">
                                <label for="inputCity" class="form-label">City</label>
                                <input type="text" class="form-control" id="inputCity">
                            </div>
                            <div class="col-12">
                                <label for="inputState" class="form-label">How did you reach us ?</label>
                                <select id="inputState" class="form-select">
                                    <option selected>Choose...</option>
                                    <option>Twitter</option>
                                    <option>Linkedin</option>
                                    <option>Instagram</option>
                                </select>
                            </div>
                            <div class="col-12">
                                <button type="submit" class="btn btn-primary">Send</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
    '''

FAKE_DB_PAGES=[
    {"url": "contact",  "detail": CONTACT_DETAILS,"title":"Contact"},
    {"url": "index",  "detail": CONTACT_DETAILS,"title":"Home"},
    {"url": "about",  "detail": CONTACT_DETAILS,"title":"About"},
]

