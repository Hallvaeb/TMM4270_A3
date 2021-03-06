

class FormCreator(object):
    # Made a class so making multiple versions of the form and switching between is easy,
    # should one want for example separate forms for private or company customers...

    def get_form_private_customer(radius_list):
            # This returns a predefined form
            return """<form action="/reciept" method="post">
                    <h2>We're ready to take your order!</h2>
                    <fieldset>
                        <legend>Contact information</legend>
                        <label for="customer_name">Full name</label><br>
                        <input type="text" name="customer_name" id="customer_name" placeholder="Your name, sir" ><br>
                        <label for="address">Address</label><br>
                        <input type="text" name="address" placeholder=".. For delivery, not visits.." id="address"><br>
                        <label for="phone">Phone</label><br>
                        <input type="number" name="phone" placeholder="Phone" id="phone"><br>
                        <label for="email">E-mail</label><br>
                        <input class="last" type="email" name="email" placeholder="E-mail" id="email" required 
                            oninvalid="this.setCustomValidity('Email req. as it is used as customer key in db')" oninput="this.setCustomValidity('')"><br>
                    </fieldset>
                    <fieldset>
                        <legend>Gear specifications</legend>
                        <label for="material">Material </label><br>
                        <select id= material" name= material">
                            <option value="" disabled selected>Material</option>
                            <option>Brass</option>
                            <option>Steel</option>
                            <option selected="selected">Diamond</option>
                            <option>Uncertain</option>
                        </select><br>
                        <label for="color">Color</label><br>
                        <select id="color" name="color">
                            <option value="" disabled selected>Color</option>
                            <option selected="selected">None</option>
                            <option>Have it painted</option>
                            <option>Uncertain</option>
                        </select><br>
                    </fieldset>
                    <input type="hidden" name="radius_list" value='"""+FormCreator.list_to_string(radius_list)+"""'>
                    <input type="submit" value="Order now!" id="submit">
                    </form></section>"""


    def get_form_private_customer_DUMMY(radius_list):
            # This returns a ALREADY VALUED form for faster testing
            form = """<form action="/reciept" method="post">
                    <h2>We're ready to take your order!</h2>
                    <fieldset>
                        <legend>Contact information</legend>
                        <label for="customer_name">Full name</label><br>
                        <input type="text" name="customer_name" id="customer_name" placeholder="Your name, sir" value="Test Lobov"><br>
                        <label for="address">Address</label><br>
                        <input type="text" name="address" placeholder=".. For delivery, not visits.." id="address" value="Testing street 10"><br>
                        <label for="phone">Phone</label><br>
                        <input type="number" name="phone" placeholder="Phone" id="phone" value="01234567"><br>
                        <label for="email">E-mail</label><br>
                        <input class="last" type="email" name="email" placeholder="E-mail" id="email" required 
                            oninvalid="this.setCustomValidity('Email req. as it is used as customer key in db')" oninput="this.setCustomValidity('')" 
                            value="test_email@gmail.com"><br>
                    </fieldset>
                    <fieldset>
                        <legend>Gear specifications</legend>
                        <label for="material">Material </label><br>
                        <select id= material" name= material">
                            <option value="" disabled selected>Material</option>
                            <option>Brass</option>
                            <option>Steel</option>
                            <option selected="selected" >Diamond</option>
                            <option>Uncertain</option>
                        </select><br>
                        <label for="color">Color</label><br>
                        <select id="color" name="color">
                            <option value="" disabled selected>Color</option>
                            <option selected="selected">None</option>
                            <option>Have it painted</option>
                            <option>Uncertain</option>
                        </select><br>
                    </fieldset>
                    <input type="hidden" name="radius_list" value=\""""+FormCreator.list_to_string(radius_list)+"""\">
                    <input type="submit" value="Order now!" id="submit">
                    </form></section>"""
            return form
                    
    def get_form_set_radiuses(n_gears):
        out = """
        <form action = "/review" method="post">
			"""+str(n_gears)+" gears chosen! Choose the radiuses:<br><br>"""

		# Making a field for each gear radius
        for i in range(int(n_gears)): # n_gears
                out += "<label for='gear'" + str(i) + "> Gear " + str(i+1) + ": </label>"
                out +="""
                <input type = "number" pattern="0123456789" id = '""" + str(i) + """' 
                    name = '"gear" """ + str(i) +""" ' placeholder = "Radius [mm]" 
                    autofocus required> <br><br> """

        # Add submit button at the end and end form
        out += """<input type="submit" value="Submit"></form>"""
        return out


    get_form_n_gears = """<form action = '/setRadius' method='post'>
						<label for='n_gears'>How many gears do you want?</label><br><br>
						<input pattern='0123456789' type='number' name='n_gears' id='n_gears' autofocus required><br><br>
						<input type='submit' value='submit'><br>
					</form>"""

    def list_to_string(radius_list):
        return str(radius_list).replace("%5B", "[").replace("%2C", ",").replace("%5D", "]")