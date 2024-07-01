from typing import Literal

type MtlCss = str
global_value = Literal["inherit", "initial", "revert", "revert-layer", "unset"]


def display(
    value: Literal[
        "block",
        "inline",
        "inline-block",
        "flex",
        "inline-flex",
        "grid",
        "inline-grid",
        "flow-root",
        "none",
        "contents",
        "block flex",
        "block flow",
        "block flow-root",
        "block grid",
        "inline flex",
        "inline flow",
        "inline flow-root",
        "inline grid",
        "table",
        "table-row",
        "list-item",
        global_value,
    ]
):
    return f"display: {value};"


def dis(
    value: Literal[
        "block",
        "inline",
        "inline-block",
        "flex",
        "inline-flex",
        "grid",
        "inline-grid",
        "flow-root",
        "none",
        "contents",
        "block flex",
        "block flow",
        "block flow-root",
        "block grid",
        "inline flex",
        "inline flow",
        "inline flow-root",
        "inline grid",
        "table",
        "table-row",
        "list-item",
        global_value,
    ]
):
    return f"display: {value};"


def flex():
    return "display: flex;"


def grid():
    return "display: grid;"


def fBasic(value):
    return f"flex-basics: {value};"


def fDir(
    value: Literal["row", "row-reverse", "column", "column-reverse", global_value]
):
    return f"flex-direction: {value};"


def fWarp(value: Literal["warp", "warp-reverse", "nowarp", global_value]):
    return f"flex-wrap: {value};"


def fControl(value: str):
    return f"flex: {value};"


def fGrow(value: str):
    return f"flex-grow: {value};"


def fShrink(value: str):
    return f"flex-shrink: {value};"


def order(value: str):
    return f"order: {value};"


def gCols(props: Literal["repeat", "r", "none", "n"], value: str):
    match props:
        case "repeat" | "r":
            return f"grid-template-columns: repeat({value}, minmax(0, 1fr));"
        case "none" | "n":
            return f"grid-template-columns: {value};"
        case _:
            return f"grid-template-columns: {value};"


def gCol(props: Literal["none", "n", "start", "s", "end", "e"], value: str):
    match props:
        case "none" | "n":
            return f"grid-column: {value};"
        case "start" | "s":
            return f"grid-column-start: {value};"
        case "end" | "e":
            return f"grid-column-end: {value};"
        case _:
            return f"grid-column: {value};"


def gRows(props: Literal["repeat", "r", "none", "n"], value: str):
    match props:
        case "repeat" | "r":
            return f"grid-template-rows: repeat({value}, minmax(0, 1fr));"
        case "none" | "n":
            return f"grid-template-rows: {value};"
        case _:
            return f"grid-template-rows: {value};"


def gRow(props: Literal["none", "n", "start", "s", "end", "e"], value: str):
    match props:
        case "none" | "n":
            return f"grid-row: {value};"
        case "start" | "s":
            return f"grid-row-start: {value};"
        case "end" | "e":
            return f"grid-row-end: {value};"
        case _:
            return f"grid-row: {value};"


def gFlowRow(value: Literal["row", "column", "dense", "row dense", "column dense"]):
    return f"grid-auto-flow: {value};"


def gAutoCols(value: str):
    return f"grid-auto-column: {value};"


def gAutoRows(value: str):
    return f"grid-auto-rows: {value};"


def gap(props: Literal["column", "c", "x", "row", "r", "y", "none", "n"], value: str):
    match props:
        case "column" | "c" | "x":
            return f"column-gap: {value};"
        case "row" | "r" | "y":
            return f"row-gap: {value};"
        case "none" | "n":
            return f"gap: {value};"
        case _:
            return f"gap: {value};"


def justifyContent(
    value: Literal[
        "center",
        "start",
        "end",
        "flex-start",
        "flex-end",
        "left",
        "right",
        "normal",
        "space-between",
        "space-around",
        "space-evenly",
        "stretch",
        "safe center",
        "unsafe center",
        global_value,
    ]
):
    return f"justify-content: {value};"


def justifyItems(
    value: Literal[
        "normal",
        "stretch",
        "center",
        "end",
        "flex-start",
        "flex-end",
        "self-start",
        "self-end",
        "left",
        "right",
        "anchor-center",
        "baseline",
        "first baseline",
        "last baseline",
        "safe center",
        "unsafe center",
        global_value,
    ]
):
    return f"justify-items: {value};"


def justifySelf(
    value: Literal[
        "auto",
        "normal",
        "stretch",
        "center",
        "start",
        "end",
        "flex-start",
        "flex-end",
        "self-start",
        "self-end",
        "left",
        "right",
        "anchor-center",
        "baseline",
        "first baseline",
        "last baseline",
        "safe center",
        "unsafe center",
        global_value,
    ]
):
    return f"justify-self: {value};"


def alignContent(
    value: Literal[
        "center",
        "start",
        "end",
        "flex-start",
        "flex-end",
        "left",
        "right",
        "normal",
        "space-between",
        "space-around",
        "space-evenly",
        "stretch",
        "safe center",
        "unsafe center",
        global_value,
    ]
):
    return f"align-content: {value};"


def alignItems(
    value: Literal[
        "normal",
        "stretch",
        "center",
        "end",
        "flex-start",
        "flex-end",
        "self-start",
        "self-end",
        "left",
        "right",
        "anchor-center",
        "baseline",
        "first baseline",
        "last baseline",
        "safe center",
        "unsafe center",
        global_value,
    ]
):
    return f"align-items: {value};"


def alignSelf(
    value: Literal[
        "auto",
        "normal",
        "stretch",
        "center",
        "start",
        "end",
        "flex-start",
        "flex-end",
        "self-start",
        "self-end",
        "left",
        "right",
        "anchor-center",
        "baseline",
        "first baseline",
        "last baseline",
        "safe center",
        "unsafe center",
        global_value,
    ]
):
    return f"align-self: {value};"


def placeContent(
    value: Literal[
        "center start",
        "start center",
        "end left",
        "flex-start center",
        "flex-end center",
        "baseline center",
        "first baseline space-evenly",
        "last baseline right",
        "space-between space-evenly",
        "space-around space-evenly",
        "space-evenly stretch",
        "stretch space-evenly",
        global_value,
    ]
):
    return f"place-content: {value};"


def placeItems(
    value: Literal[
        "center",
        "normal start",
        "center normal",
        "start legacy",
        "end normal",
        "self-start legacy",
        "self-end normal",
        "flex-start legacy",
        "flex-end normal",
        "anchor-center",
        "baseline normal",
        "first baseline legacy",
        "last baseline normal",
        "stretch legacy",
        global_value,
    ]
):
    return f"place-items: {value};"


def placeSelf(
    value: Literal[
        "auto center",
        "normal start",
        "center normal",
        "start auto",
        "end normal",
        "self-start auto",
        "self-end normal",
        "flex-start auto",
        "flex-end normal",
        "anchor-center",
        "baseline normal",
        "first baseline auto",
        "last baseline normal",
        "stretch auto",
        global_value,
    ]
):
    return f"place-self: {value};"


def useMtlCss(styles: list[MtlCss]):
    temp_style = ""
    for style in styles:
        temp_style += style + " "
    return temp_style


print(useMtlCss([dis("flex")]))
