XPath locator examples

To find the link in this page:

    <html><body>
    <p>The fox jumped over the lazy brown <a href="dogs.html">dog</a>.</p>
    </body></html>

A raw XPath traverses the hierarchy from the root element of the document (page) to the desired element:

    /html/body/p/a

 
Child of Element ID

XPath can find an element by ID like this:

    //*[@id="element_id"]

So if you need to find an element that is near another element with an ID, like the link in this example:

    <html><body>
    <p id="fox">The fox jumped over the lazy brown <a href="dogs.html">dog</a>.</p>
    </body></html>

you could try an XPath like this to find the first link that is a child of the element with ID=”fox”:

    //*[@id="fox"]/a

 
Button Text

There are two ways to declare a standard button in HTML, discounting the many ways to make something that looks like a button, but is not. To determine how an element is declared in the HTML, see how to inspect an element in the browser.

If the button is declared with the <button> tag and the button says “press me”, try this:

    //button(contains(., 'press me')]

If the button is a form submit button (declared with the <input> tag and type=”submit” or =”button”) and says “press me”, try this:

    //input[@value='press me']

 
Text of element

Sometimes a bit of text is styled as a link or button. To find it, try this:

    //*[text()='the visible text']

 
The Nth element

To find the Nth element, you must surround your XPath in ()s and then specify the Nth using [n], like this:

    (xpath)[n]

A very simple example – find the 3rd link on a page:

    (//a)[3]

To find the 4rd text input field on a page:

    (//input[@type="text"])[4]

You can also traverse from the indexed element. So, to find the link in the 2nd div with class ‘abc’:

    (//div[@class='abc'])[2]/a