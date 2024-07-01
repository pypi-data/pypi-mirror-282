import mtl.tags as tag
import mtl.attribute as attr


class Page:
    def __init__(self, *components: str):
        self.components = components
        self.component = ""
        self.__loopComponent()

    def remComponent(ref):
        pass

    def __loopComponent(self) -> str:
        temp_string = ""
        for component in self.components:
            temp_string += component

        self.component = temp_string

    def getComponent(self):
        return self.component


# *****
# TAG
# *****
def pack(*contents):
    temp_content = ""
    for content in contents:
        temp_content += content
    return str(temp_content)


def a(*contents, props: list = [""], ref: str = ""):
    return tag.htm("a", *contents, props=props, ref=ref)


def abbr(*contents, props: list = [""], ref: str = ""):
    return tag.htm("abbr", *contents, props=props, ref=ref)


def address(*contents, props: list = [""], ref: str = ""):
    return tag.htm("address", *contents, props=props, ref=ref)


def area(*contents, props: list = [""], ref: str = ""):
    return tag.htm("area", *contents, props=props, ref=ref)


def article(*contents, props: list = [""], ref: str = ""):
    return tag.htm("article", *contents, props=props, ref=ref)


def aside(*contents, props: list = [""], ref: str = ""):
    return tag.htm("aside", *contents, props=props, ref=ref)


def audio(*contents, props: list = [""], ref: str = ""):
    return tag.htm("audio", *contents, props=props, ref=ref)


def b(*contents, props: list = [""], ref: str = ""):
    return tag.htm("b", *contents, props=props, ref=ref)


def base(*contents, props: list = [""], ref: str = ""):
    return tag.htm("base", *contents, props=props, ref=ref)


def bdi(*contents, props: list = [""], ref: str = ""):
    return tag.htm("bdi", *contents, props=props, ref=ref)


def bdo(*contents, props: list = [""], ref: str = ""):
    return tag.htm("bdo", *contents, props=props, ref=ref)


def blockquote(*contents, props: list = [""], ref: str = ""):
    return tag.htm("blockquote", *contents, props=props, ref=ref)


def body(*contents, props: list = [""], ref: str = ""):
    return tag.htm("body", *contents, props=props, ref=ref)


def br(*contents, props: list = [""], ref: str = ""):
    return tag.htm("br", *contents, props=props, ref=ref)


def button(*contents, props: list = [""], ref: str = ""):
    return tag.htm("button", *contents, props=props, ref=ref)


def canvas(*contents, props: list = [""], ref: str = ""):
    return tag.htm("canvas", *contents, props=props, ref=ref)


def caption(*contents, props: list = [""], ref: str = ""):
    return tag.htm("caption", *contents, props=props, ref=ref)


def cite(*contents, props: list = [""], ref: str = ""):
    return tag.htm("cite", *contents, props=props, ref=ref)


def code(*contents, props: list = [""], ref: str = ""):
    return tag.htm("code", *contents, props=props, ref=ref)


def col(*contents, props: list = [""], ref: str = ""):
    return tag.htm("col", *contents, props=props, ref=ref)


def colgroup(*contents, props: list = [""], ref: str = ""):
    return tag.htm("colgroup", *contents, props=props, ref=ref)


def data(*contents, props: list = [""], ref: str = ""):
    return tag.htm("data", *contents, props=props, ref=ref)


def datalist(*contents, props: list = [""], ref: str = ""):
    return tag.htm("datalist", *contents, props=props, ref=ref)


def dd(*contents, props: list = [""], ref: str = ""):
    return tag.htm("dd", *contents, props=props, ref=ref)


def dele(*contents, props: list = [""], ref: str = ""):
    return tag.htm("del", *contents, props=props, ref=ref)


def details(*contents, props: list = [""], ref: str = ""):
    return tag.htm("details", *contents, props=props, ref=ref)


def dfn(*contents, props: list = [""], ref: str = ""):
    return tag.htm("dfn", *contents, props=props, ref=ref)


def dialog(*contents, props: list = [""], ref: str = ""):
    return tag.htm("dialog", *contents, props=props, ref=ref)


def div(*contents, props: list = [""], ref: str = ""):
    return tag.htm("div", *contents, props=props, ref=ref)


def dl(*contents, props: list = [""], ref: str = ""):
    return tag.htm("dl", *contents, props=props, ref=ref)


def dt(*contents, props: list = [""], ref: str = ""):
    return tag.htm("dt", *contents, props=props, ref=ref)


def em(*contents, props: list = [""], ref: str = ""):
    return tag.htm("em", *contents, props=props, ref=ref)


def embed(*contents, props: list = [""], ref: str = ""):
    return tag.htm("embed", *contents, props=props, ref=ref)


def fieldset(*contents, props: list = [""], ref: str = ""):
    return tag.htm("fieldset", *contents, props=props, ref=ref)


def figcaption(*contents, props: list = [""], ref: str = ""):
    return tag.htm("figcaption", *contents, props=props, ref=ref)


def figure(*contents, props: list = [""], ref: str = ""):
    return tag.htm("figure", *contents, props=props, ref=ref)


def footer(*contents, props: list = [""], ref: str = ""):
    return tag.htm("footer", *contents, props=props, ref=ref)


def form(*contents, props: list = [""], ref: str = ""):
    return tag.htm("form", *contents, props=props, ref=ref)


def h1(*contents, props: list = [""], ref: str = ""):
    return tag.htm("h1", *contents, props=props, ref=ref)


def h2(*contents, props: list = [""], ref: str = ""):
    return tag.htm("h2", *contents, props=props, ref=ref)


def h3(*contents, props: list = [""], ref: str = ""):
    return tag.htm("h3", *contents, props=props, ref=ref)


def h4(*contents, props: list = [""], ref: str = ""):
    return tag.htm("h4", *contents, props=props, ref=ref)


def h5(*contents, props: list = [""], ref: str = ""):
    return tag.htm("h5", *contents, props=props, ref=ref)


def h6(*contents, props: list = [""], ref: str = ""):
    return tag.htm("h6", *contents, props=props, ref=ref)


def head(*contents, props: list = [""], ref: str = ""):
    return tag.htm("head", *contents, props=props, ref=ref)


def header(*contents, props: list = [""], ref: str = ""):
    return tag.htm("header", *contents, props=props, ref=ref)


def hgroup(*contents, props: list = [""], ref: str = ""):
    return tag.htm("hgroup", *contents, props=props, ref=ref)


def hr(*contents, props: list = [""], ref: str = ""):
    return tag.htm("hr", *contents, props=props, ref=ref)


def html(*contents, props: list = [""], ref: str = ""):
    return tag.htm("html", *contents, props=props, ref=ref)


def i(*contents, props: list = [""], ref: str = ""):
    return tag.htm("i", *contents, props=props, ref=ref)


def iframe(*contents, props: list = [""], ref: str = ""):
    return tag.htm("iframe", *contents, props=props, ref=ref)


def img(*contents, props: list = [""], ref: str = ""):
    return tag.htm("img", *contents, props=props, ref=ref)


def input(*contents, props: list = [""], ref: str = ""):
    return tag.htm("input", *contents, props=props, ref=ref)


def ins(*contents, props: list = [""], ref: str = ""):
    return tag.htm("ins", *contents, props=props, ref=ref)


def kbd(*contents, props: list = [""], ref: str = ""):
    return tag.htm("kbd", *contents, props=props, ref=ref)


def lable(*contents, props: list = [""], ref: str = ""):
    return tag.htm("lable", *contents, props=props, ref=ref)


def legend(*contents, props: list = [""], ref: str = ""):
    return tag.htm("legend", *contents, props=props, ref=ref)


def li(*contents, props: list = [""], ref: str = ""):
    return tag.htm("li", *contents, props=props, ref=ref)


def link(*contents, props: list = [""], ref: str = ""):
    return tag.htm("link", *contents, props=props, ref=ref)


def main(*contents, props: list = [""], ref: str = ""):
    return tag.htm("main", *contents, props=props, ref=ref)


def map(*contents, props: list = [""], ref: str = ""):
    return tag.htm("map", *contents, props=props, ref=ref)


def mark(*contents, props: list = [""], ref: str = ""):
    return tag.htm("mark", *contents, props=props, ref=ref)


def menu(*contents, props: list = [""], ref: str = ""):
    return tag.htm("menu", *contents, props=props, ref=ref)


def meta(*contents, props: list = [""], ref: str = ""):
    return tag.htm("meta", *contents, props=props, ref=ref)


def meter(*contents, props: list = [""], ref: str = ""):
    return tag.htm("meter", *contents, props=props, ref=ref)


def nav(*contents, props: list = [""], ref: str = ""):
    return tag.htm("nav", *contents, props=props, ref=ref)


def noscript(*contents, props: list = [""], ref: str = ""):
    return tag.htm("noscript", *contents, props=props, ref=ref)


def obj(*contents, props: list = [""], ref: str = ""):
    return tag.htm("object", *contents, props=props, ref=ref)


def ol(*contents, props: list = [""], ref: str = ""):
    return tag.htm("ol", *contents, props=props, ref=ref)


def optgroup(*contents, props: list = [""], ref: str = ""):
    return tag.htm("optgroup", *contents, props=props, ref=ref)


def option(*contents, props: list = [""], ref: str = ""):
    return tag.htm("option", *contents, props=props, ref=ref)


def output(*contents, props: list = [""], ref: str = ""):
    return tag.htm("output", *contents, props=props, ref=ref)


def p(*contents, props: list = [""], ref: str = ""):
    return tag.htm("p", *contents, props=props, ref=ref)


def param(*contents, props: list = [""], ref: str = ""):
    return tag.htm("param", *contents, props=props, ref=ref)


def picture(*contents, props: list = [""], ref: str = ""):
    return tag.htm("picture", *contents, props=props, ref=ref)


def pre(*contents, props: list = [""], ref: str = ""):
    return tag.htm("pre", *contents, props=props, ref=ref)


def progress(*contents, props: list = [""], ref: str = ""):
    return tag.htm("progress", *contents, props=props, ref=ref)


def q(*contents, props: list = [""], ref: str = ""):
    return tag.htm("q", *contents, props=props, ref=ref)


def rp(*contents, props: list = [""], ref: str = ""):
    return tag.htm("rp", *contents, props=props, ref=ref)


def rt(*contents, props: list = [""], ref: str = ""):
    return tag.htm("rt", *contents, props=props, ref=ref)


def ruby(*contents, props: list = [""], ref: str = ""):
    return tag.htm("ruby", *contents, props=props, ref=ref)


def s(*contents, props: list = [""], ref: str = ""):
    return tag.htm("s", *contents, props=props, ref=ref)


def samp(*contents, props: list = [""], ref: str = ""):
    return tag.htm("samp", *contents, props=props, ref=ref)


def script(*jsFuntion, props: list = [""], ref: str = ""):
    return tag.htm("script", *jsFuntion, props=props, ref=ref)


def search(*contents, props: list = [""], ref: str = ""):
    return tag.htm("search", *contents, props=props, ref=ref)


def section(*contents, props: list = [""], ref: str = ""):
    return tag.htm("section", *contents, props=props, ref=ref)


def select(*contents, props: list = [""], ref: str = ""):
    return tag.htm("select", *contents, props=props, ref=ref)


def small(*contents, props: list = [""], ref: str = ""):
    return tag.htm("small", *contents, props=props, ref=ref)


def source(*contents, props: list = [""], ref: str = ""):
    return tag.htm("source", *contents, props=props, ref=ref)


def span(*contents, props: list = [""], ref: str = ""):
    return tag.htm("span", *contents, props=props, ref=ref)


def strong(*contents, props: list = [""], ref: str = ""):
    return tag.htm("strong", *contents, props=props, ref=ref)


def styles(*style, props: list = [""], ref: str = ""):
    return tag.htm("style", *style, props=props, ref=ref)


def sub(*contents, props: list = [""], ref: str = ""):
    return tag.htm("sub", *contents, props=props, ref=ref)


def summary(*contents, props: list = [""], ref: str = ""):
    return tag.htm("summary", *contents, props=props, ref=ref)


def sup(*contents, props: list = [""], ref: str = ""):
    return tag.htm("sup", *contents, props=props, ref=ref)


def svg(*contents, props: list = [""], ref: str = ""):
    return tag.htm("svg", *contents, props=props, ref=ref)


def table(*contents, props: list = [""], ref: str = ""):
    return tag.htm("table", *contents, props=props, ref=ref)


def tbody(*contents, props: list = [""], ref: str = ""):
    return tag.htm("tbody", *contents, props=props, ref=ref)


def td(*contents, props: list = [""], ref: str = ""):
    return tag.htm("td", *contents, props=props, ref=ref)


def template(*contents, props: list = [""], ref: str = ""):
    return tag.htm("template", *contents, props=props, ref=ref)


def textarea(*contents, props: list = [""], ref: str = ""):
    return tag.htm("textarea", *contents, props=props, ref=ref)


def tfoot(*contents, props: list = [""], ref: str = ""):
    return tag.htm("tfoot", *contents, props=props, ref=ref)


def th(*contents, props: list = [""], ref: str = ""):
    return tag.htm("th", *contents, props=props, ref=ref)


def thead(*contents, props: list = [""], ref: str = ""):
    return tag.htm("thead", *contents, props=props, ref=ref)


def time(*contents, props: list = [""], ref: str = ""):
    return tag.htm("time", *contents, props=props, ref=ref)


def title(*contents, props: list = [""], ref: str = ""):
    return tag.htm("title", *contents, props=props, ref=ref)


def tr(*contents, props: list = [""], ref: str = ""):
    return tag.htm("tr", *contents, props=props, ref=ref)


def track(*contents, props: list = [""], ref: str = ""):
    return tag.htm("track", *contents, props=props, ref=ref)


def u(*contents, props: list = [""], ref: str = ""):
    return tag.htm("u", *contents, props=props, ref=ref)


def ul(*contents, props: list = [""], ref: str = ""):
    return tag.htm("ul", *contents, props=props, ref=ref)


def var(*contents, props: list = [""], ref: str = ""):
    return tag.htm("var", *contents, props=props, ref=ref)


def video(*contents, props: list = [""], ref: str = ""):
    return tag.htm("video", *contents, props=props, ref=ref)


def wbr(*contents, props: list = [""], ref: str = ""):
    return tag.htm("wbr", *contents, props=props, ref=ref)


# ******
# ATTR
# ******


def accept(props: str):
    return attr.attr("accept", props)


def acceptCharset(props: str):
    return attr.attr("accept-charset")


def accessKey(props: str):
    return attr.attr("accesskey", props)


def action(props: str):
    return attr.attr("action", props)


def alt(props: str):
    return attr.attr("alt", props)


def asyncScript(props: str):
    return attr.attr("async", props)


def autocomplete(props: str):
    return attr.attr("autocomplete", props)


def autofocus(props: str):
    return attr.attr("autofocus", props)


def autoplay(props: str):
    return attr.attr("autoplay", props)


def charset(props: str):
    return attr.attr("charset", props)


def checked(props: str):
    return attr.attr("checked", props)


def cite(props: str):
    return attr.attr("cite", props)


def className(props: str):
    return attr.attr("class", props)


def cols(props: str):
    return attr.attr("cols", props)


def colspan(props: str):
    return attr.attr("colspan", props)


def content(props: str):
    return attr.attr("content", props)


def contenteditable(props: str):
    return attr.attr("contenteditable", props)


def controls(props: str):
    return attr.attr("controls", props)


def coords(props: str):
    return attr.attr("coords", props)


def data(props: str):
    return attr.attr("data", props)


def newData(dataName, props: str):
    return attr.attr(f"data-{dataName}", props)


def datetime(props: str):
    return attr.attr("datetime", props)


def default(props: str):
    return attr.attr("default", props)


def defer(props: str):
    return attr.attr("defer", props)


def dir(props: str):
    return attr.attr("dir", props)


def dirname(props: str):
    return attr.attr("dirname", props)


def disabled(props: str):
    return attr.attr("disabled", props)


def download(props: str):
    return attr.attr("download", props)


def draggable(props: str):
    return attr.attr("draggable", props)


def enctype(props: str):
    return attr.attr("enctype", props)


def enterKeyHint(props: str):
    return attr.attr("enterkeyhint", props)


def htmlFor(props: str):
    return attr.attr("for", props)


def form(props: str):
    return attr.attr("form", props)


def formAction(props: str):
    return attr.attr("formaction", props)


def headers(props: str):
    return attr.attr("headers", props)


def height(props: str):
    return attr.attr("height", props)


def hidden(props: str):
    return attr.attr("hidden", props)


def high(props: str):
    return attr.attr("high", props)


def href(props: str):
    return attr.attr("href", props)


def hrefLang(props: str):
    return attr.attr("hreflang", props)


def httpEquiv(props: str):
    return attr.attr("http-equiv", props)


def id(props: str):
    return attr.attr("id", props)


def inert(props: str):
    return attr.attr("inert", props)


def inputMode(props: str):
    return attr.attr("inputmode", props)


def ismap(props: str):
    return attr.attr("ismap", props)


def kind(props: str):
    return attr.attr("kind", props)


def label(props: str):
    return attr.attr("label", props)


def lang(props: str):
    return attr.attr("lang", props)


def lists(props: str):
    return attr.attr("list", props)


def loop(props: str):
    return attr.attr("loop", props)


def low(props: str):
    return attr.attr("low", props)


def max(props: str):
    return attr.attr("max", props)


def maxLength(props: str):
    return attr.attr("maxlength", props)


def media(props: str):
    return attr.attr("media", props)


def method(props: str):
    return attr.attr("method", props)


def min(props: str):
    return attr.attr("min", props)


def multiple(props: str):
    return attr.attr("multiple", props)


def muted(props: str):
    return attr.attr("muted", props)


def name(props: str):
    return attr.attr("name", props)


def novalidate(props: str):
    return attr.attr("novalidate", props)


def onAbort(props: str):
    return attr.attr("onabort", props)


def onAfterPrint(props: str):
    return attr.attr("onafterprint", props)


def onBeforePrint(props: str):
    return attr.attr("onbeforeprint", props)


def onBeforeUnload(props: str):
    return attr.attr("onbeforeunload", props)


def onBlur(props: str):
    return attr.attr("onblur", props)


def onCanplay(props: str):
    return attr.attr("oncanplay", props)


def onCanplaythrough(props: str):
    return attr.attr("oncanplaythrough", props)


def onChange(props: str):
    return attr.attr("onchange", props)


def onClick(props: str):
    return attr.attr("onclick", props)


def onContextMenu(props: str):
    return attr.attr("oncontextmenu", props)


def onCopy(props: str):
    return attr.attr("oncopy", props)


def onCueChange(props: str):
    return attr.attr("oncuechange", props)


def onCut(props: str):
    return attr.attr("oncut", props)


def onDubbleClick(props: str):
    return attr.attr("ondblclick", props)


def onDrag(props: str):
    return attr.attr("ondrag", props)


def onDragEnd(props: str):
    return attr.attr("ondragend", props)


def onDragEnter(props: str):
    return attr.attr("ondragenter", props)


def onDragLeave(props: str):
    return attr.attr("ondragleave", props)


def onDragOver(props: str):
    return attr.attr("ondragover", props)


def onDragStart(props: str):
    return attr.attr("ondragstart", props)


def onDrop(props: str):
    return attr.attr("ondrop", props)


def onDurationChange(props: str):
    return attr.attr("ondurationchange", props)


def onEmptied(props: str):
    return attr.attr("onemptied", props)


def onEnded(props: str):
    return attr.attr("onended", props)


def onError(props: str):
    return attr.attr("onerror", props)


def onFocus(props: str):
    return attr.attr("onfocus", props)


def onHashChange(props: str):
    return attr.attr("onhashchange", props)


def onInput(props: str):
    return attr.attr("oninput", props)


def onInvalid(props: str):
    return attr.attr("oninvalid", props)


def onKeyDown(props: str):
    return attr.attr("onkeydown", props)


def onKeyPress(props: str):
    return attr.attr("onkeypress", props)


def onKeyUp(props: str):
    return attr.attr("onkeyup", props)


def onLoad(props: str):
    return attr.attr("onload", props)


def onLoadedData(props: str):
    return attr.attr("onloadeddata", props)


def onLoadedMetadata(props: str):
    return attr.attr("onloadedmetadata", props)


def onLoadStart(props: str):
    return attr.attr("onloadstart", props)


def onMouseDown(props: str):
    return attr.attr("onmousedown", props)


def onMouseMove(props: str):
    return attr.attr("onmousemove", props)


def onMouseOut(props: str):
    return attr.attr("onmouseout", props)


def onMouseOver(props: str):
    return attr.attr("onmouseover", props)


def onMouseUp(props: str):
    return attr.attr("onmouseup", props)


def onMouseWheel(props: str):
    return attr.attr("onmousewheel", props)


def onOffline(props: str):
    return attr.attr("onoffline", props)


def onOnline(props: str):
    return attr.attr("ononline", props)


def onPageHide(props: str):
    return attr.attr("onpagehide", props)


def onPageShow(props: str):
    return attr.attr("onpageshow", props)


def onPaste(props: str):
    return attr.attr("onpaste", props)


def onPause(props: str):
    return attr.attr("onpause", props)


def onPlay(props: str):
    return attr.attr("onplay", props)


def onPlaying(props: str):
    return attr.attr("onplaying", props)


def onPopState(props: str):
    return attr.attr("onpopstate", props)


def onProgress(props: str):
    return attr.attr("onprogress", props)


def onRateChange(props: str):
    return attr.attr("onratechange", props)


def onReset(props: str):
    return attr.attr("onreset", props)


def onResize(props: str):
    return attr.attr("onresize", props)


def onScroll(props: str):
    return attr.attr("onscroll", props)


def onSearch(props: str):
    return attr.attr("onsearch", props)


def onsSeked(props: str):
    return attr.attr("onseeked", props)


def onSeeking(props: str):
    return attr.attr("onseeking", props)


def onSelect(props: str):
    return attr.attr("onselect", props)


def onStalled(props: str):
    return attr.attr("onstalled", props)


def onStorage(props: str):
    return attr.attr("onstorage", props)


def onSubmit(props: str):
    return attr.attr("onsubmit", props)


def onSuspend(props: str):
    return attr.attr("onsuspend", props)


def onTimeUpdate(props: str):
    return attr.attr("ontimeupdate", props)


def onToggle(props: str):
    return attr.attr("ontoggle", props)


def onUnLoad(props: str):
    return attr.attr("onunload", props)


def onVolumeChange(props: str):
    return attr.attr("onvolumechange", props)


def onWaiting(props: str):
    return attr.attr("onwaiting", props)


def onWheel(props: str):
    return attr.attr("onwheel", props)


def opens(props: str):
    return attr.attr("open", props)


def optimum(props: str):
    return attr.attr("optimum", props)


def pattern(props: str):
    return attr.attr("pattern", props)


def placeholder(props: str):
    return attr.attr("placeholder", props)


def popover(props: str):
    return attr.attr("popover", props)


def popoverTarget(props: str):
    return attr.attr("popovertarget", props)


def popoverTargetAction(props: str):
    return attr.attr("popovertargetaction", props)


def poster(props: str):
    return attr.attr("poster", props)


def preload(props: str):
    return attr.attr("preload", props)


def readonly(props: str):
    return attr.attr("readonly", props)


def rel(props: str):
    return attr.attr("rel", props)


def required(props: str):
    return attr.attr("required", props)


def reversed(props: str):
    return attr.attr("reversed", props)


def rows(props: str):
    return attr.attr("rows", props)


def rowspan(props: str):
    return attr.attr("rowspan", props)


def sandbox(props: str):
    return attr.attr("sandbox", props)


def scope(props: str):
    return attr.attr("scope", props)


def selected(props: str):
    return attr.attr("selected", props)


def shape(props: str):
    return attr.attr("shape", props)


def size(props: str):
    return attr.attr("size", props)


def sizes(props: str):
    return attr.attr("sizes", props)


def span(props: str):
    return attr.attr("span", props)


def spellcheck(props: str):
    return attr.attr("spellcheck", props)


def src(props: str):
    return attr.attr("src", props)


def srcdoc(props: str):
    return attr.attr("srcdoc", props)


def srclang(props: str):
    return attr.attr("srclang", props)


def srcset(props: str):
    return attr.attr("srcset", props)


def start(props: str):
    return attr.attr("start", props)


def step(props: str):
    return attr.attr("step", props)


def style(props: str):
    return attr.attr("style", props)


def tabindex(props: str):
    return attr.attr("tabindex", props)


def target(props: str):
    return attr.attr("target", props)


def title(props: str):
    return attr.attr("title", props)


def translate(props: str):
    return attr.attr("translate", props)


def type(props: str):
    return attr.attr("type", props)


def usemap(props: str):
    return attr.attr("usemap", props)


def value(props: str):
    return attr.attr("value", props)


def width(props: str):
    return attr.attr("width", props)


def wrap(props: str):
    return attr.attr("wrap", props)
