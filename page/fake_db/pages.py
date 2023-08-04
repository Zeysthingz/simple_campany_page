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
ABOUT_DETAILS='''
<div class="row">
            <!--            sağ ve soldan 2lk grıdler bos kalır offset ıkı olmasıda sagdan ıkı bosluk yana kaydırması demektır-->
            <div class="col-sm-8 offset-2">
                <h2>Our Vision</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi debitis ex incidunt iure libero,
                    mollitia porro veniam vitae. Accusamus adipisci aperiam cumque deserunt dolores, ipsa minus nulla
                    praesentium quidem, quisquam quos sapiente similique temporibus tenetur ullam vero, vitae!
                    Blanditiis dolore dolores dolorum explicabo fugit odio velit? Accusamus nam nihil rerum.</p>
                <p>Excepturi in nam non quisquam voluptatem? Asperiores dolores fugit labore! Adipisci asperiores
                    assumenda, delectus dolore doloremque dolores ea earum enim error ex hic id illum maiores
                    necessitatibus nihil nostrum officiis perferendis, possimus quidem quod, reiciendis rerum suscipit
                    tempore totam veniam voluptas voluptatibus. Ab dignissimos eos esse omnis possimus quidem
                    reprehenderit!</p>
                <p>Blanditiis consectetur et explicabo necessitatibus nesciunt quod, rerum. Beatae ipsam, iste itaque
                    minima nemo, odio optio quidem quis quo vel velit, vitae? Ab accusamus, ad aspernatur blanditiis
                    commodi consequuntur dolorem earum ex hic labore libero nam natus nesciunt perspiciatis possimus
                    praesentium quis, quisquam ratione reprehenderit sint, temporibus veritatis vitae voluptatum.</p>

                <hr>
                <h2>Our Mision</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus ad aperiam architecto commodi
                    cupiditate dolore dolorum enim exercitationem fugiat impedit in ipsam iste labore laudantium modi,
                    nesciunt optio, possimus quasi similique suscipit, tempora velit veritatis voluptatem? A, aspernatur
                    cumque delectus eius exercitationem, ipsam iusto labore laudantium molestias nemo porro
                    quisquam.</p>
                <p>Ab ad animi aperiam, aspernatur aut, beatae corporis earum et expedita incidunt ipsum magni, nobis
                    officiis perspiciatis quidem quo sint totam voluptate. Accusamus beatae deleniti fugit, ipsa
                    possimus recusandae sapiente. Beatae deserunt placeat quod recusandae repellendus? Deserunt ea
                    laboriosam natus, nihil nobis, perspiciatis porro praesentium provident quia quo tenetur,
                    voluptas?</p>
                <p>Aperiam assumenda atque corporis dicta, exercitationem ipsum laudantium maxime minus perferendis quia
                    quo repellendus reprehenderit! Ab aut corporis culpa debitis deserunt dignissimos distinctio dolorum
                    ducimus ea eligendi enim, ex expedita illo inventore iste iure minima minus modi nam neque odio
                    perferendis praesentium rerum, similique tempora totam vel voluptas! Dolorum, facere!</p>
            </div>
        </div>
'''
FAKE_DB_PAGES=[
    {"url": "contact",  "detail": CONTACT_DETAILS,"title":"Contact"},
    {"url": "index",  "detail": CONTACT_DETAILS,"title":"Home"},
    {"url": "about",  "detail": ABOUT_DETAILS,"title":"About"},
]

