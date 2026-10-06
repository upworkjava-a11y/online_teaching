"""Lesson goals for Python course chrome (UI language)."""

from __future__ import annotations

from .english_banking_bilingual import L
from .languages import LANG_CYRL, LANG_EN, LANG_RU, LANG_UZ

PYTHON_BANNER = {
    LANG_UZ: "Python o‘rganasiz — tushuntirish tanlangan tilda.",
    LANG_CYRL: "Python ўрганасиз — тушунтириш танланган тилда.",
    LANG_RU: "Учите Python — пояснения на выбранном языке.",
    LANG_EN: "Learn Python — explanations follow your UI language.",
}


def _g(uz: str, cyrl: str | None = None, ru: str | None = None, en: str | None = None) -> dict:
    return {"goal": L(uz, cyrl or uz, ru or uz, en or uz)}


PYTHON_LESSONS: dict[str, dict] = {
    "py-noldan-start": _g(
        "Python nima ekanini bilasiz va birinchi print() ni yozib ishga tushirasiz.",
        "Python нима эканини биласиз ва биринчи print() ни ёзиб ишга туширасиз.",
        "Поймёте, что такое Python, и запустите первый print().",
        "You understand what Python is and run your first print().",
    ),
    "py-noldan-run": _g(
        ".py fayl yaratib, izoh bilan skriptni ishga tushirasiz.",
        ".py файл яратиб, изоҳ билан скриптни ишга туширасиз.",
        "Создадите .py файл и запустите скрипт с комментариями.",
        "You create a .py file and run a script with comments.",
    ),
    "py-noldan-errors": _g(
        "Traceback dan xato turini va qatorni topasiz; 0 ga bo‘lishni xavfsiz yozasiz.",
        "Traceback дан хато турини ва қаторни топасиз.",
        "По traceback найдёте тип ошибки и строку.",
        "You read a traceback and handle zero-division safely.",
    ),
    "py-nima": _g(
        "Qachon Excel, qachon Python kerakligini tushuntirasiz.",
        "Қачон Excel, қачон Python кераклигини тушунтирасиз.",
        "Объясните, когда Excel, а когда Python.",
        "You explain when to use Excel vs Python.",
    ),
    "py-turlar": _g(
        "int, float, str, bool, None farqini bilasiz va tur xatosidan qochasiz.",
        "int, float, str, bool, None фарқини биласиз.",
        "Различите int, float, str, bool, None.",
        "You know int, float, str, bool, None and avoid type mistakes.",
    ),
    "py-ifodalar": _g(
        "Foiz o‘zgarish va f-string bilan hisobot matnini yozasiz.",
        "Фоиз ўзгариш ва f-string билан ҳисобот матнини ёзасиз.",
        "Посчитаете процентное изменение и оформите f-string.",
        "You compute percent change and format with f-strings.",
    ),
    "py-if": _g(
        "if/elif bilan mijoz segmentini (VIP/Regular/New) yozasiz.",
        "if/elif билан мижоз сегментини ёзасиз.",
        "Напишете сегментацию клиентов через if/elif.",
        "You write customer segmentation with if/elif.",
    ),
    "py-loop": _g(
        "for bilan ro‘yxatni aylanib yig‘indi va filtr qilasiz.",
        "for билан рўйхатни айланиб йиғинди ва фильтр қиласиз.",
        "Пройдёте список циклом for: сумма и фильтр.",
        "You loop a list with for: sum and filter.",
    ),
    "py-func": _g(
        "def bilan qayta ishlatiladigan AOV funksiyasini yozasiz.",
        "def билан қайта ишлатиладиган AOV функциясини ёзасиз.",
        "Напишете переиспользуемую функцию AOV.",
        "You write a reusable AOV function.",
    ),
    "py-collections": _g(
        "list, dict, set farqini bilasiz va unique ID olasiz.",
        "list, dict, set фарқини биласиз.",
        "Различите list, dict, set и получите unique ID.",
        "You use list, dict, set and get unique IDs.",
    ),
    "py-file": _g(
        "CSV encoding/sep muammosini tushunasiz va xavfsiz o‘qishni bilasiz.",
        "CSV encoding/sep муаммосини тушунасиз.",
        "Поймёте encoding/sep CSV и безопасное чтение.",
        "You handle CSV encoding/sep and safe reading.",
    ),
    "py-except": _g(
        "try/except bilan ValueError ni tutib, yalang‘och except dan qochasiz.",
        "try/except билан ValueError ни тутиб қоласиз.",
        "Поймаете ValueError и избежите голого except.",
        "You catch ValueError and avoid bare except.",
    ),
    "np-ndarray": _g(
        "NumPy massivi nima uchun tez ekanini tushunasiz.",
        "NumPy массиви нима учун тез эканини тушунасиз.",
        "Поймёте, почему NumPy-массив быстрый.",
        "You understand why NumPy arrays are fast.",
    ),
    "np-index": _g(
        "Boolean mask va broadcasting bilan filtr/hisob qilasiz.",
        "Boolean mask ва broadcasting билан фильтр/ҳисоб қиласиз.",
        "Отфильтруете и посчитаете через mask и broadcasting.",
        "You filter and compute with masks and broadcasting.",
    ),
    "np-nan": _g(
        "NaN ni mean dan farqlab, nanmean bilan ishlaysiz.",
        "NaN ни mean дан фарқлаб, nanmean билан ишлайсиз.",
        "Отличите NaN от mean и используете nanmean.",
        "You handle NaN with nanmean correctly.",
    ),
    "pd-df": _g(
        "DataFrame yaratib, head/dtypes/shape ni o‘qiysiz.",
        "DataFrame яратиб, head/dtypes/shape ни ўқийсиз.",
        "Создадите DataFrame и прочитаете head/dtypes/shape.",
        "You create a DataFrame and read head/dtypes/shape.",
    ),
    "pd-filter": _g(
        "Ikki shartni & bilan filtrlab yozasiz.",
        "Икки шартни & билан фильтрлаб ёзасиз.",
        "Отфильтруете двумя условиями через &.",
        "You filter with two conditions using &.",
    ),
    "pd-assign": _g(
        "Yangi ustun yaratasiz va SettingWithCopy dan qochasiz.",
        "Янги устун яратасиз ва SettingWithCopy дан қочасиз.",
        "Создадите новый столбец и избежите SettingWithCopy.",
        "You create columns safely and avoid SettingWithCopy.",
    ),
    "pd-na": _g(
        "NaN vs 0 farqini bilasiz; flag + fillna siyosatini yozasiz.",
        "NaN vs 0 фарқини биласиз.",
        "Различите NaN и 0; напишете политику fillna.",
        "You separate NaN vs 0 and define a fill policy.",
    ),
    "pd-dup": _g(
        "drop_duplicates subset bilan to‘g‘ri kalitni tanlaysiz.",
        "drop_duplicates subset билан тўғри калитни танлайсиз.",
        "Правильно выберете ключ для drop_duplicates.",
        "You choose the right key for drop_duplicates.",
    ),
    "pd-cast": _g(
        "to_numeric(errors='coerce') bilan matnni songa o‘girasiz.",
        "to_numeric(errors='coerce') билан матнни сонга ўгирасиз.",
        "Преобразуете текст в число через to_numeric(coerce).",
        "You convert text to numbers with to_numeric(coerce).",
    ),
    "pd-groupby": _g(
        "groupby + agg (sum/nunique) bilan region KPI yozasiz.",
        "groupby + agg билан region KPI ёзасиз.",
        "Посчитаете KPI по регионам через groupby + agg.",
        "You build region KPIs with groupby + agg.",
    ),
    "pd-merge": _g(
        "left merge va fan-out xavfini tushunasiz.",
        "left merge ва fan-out хавфини тушунасиз.",
        "Поймёте left merge и риск fan-out.",
        "You use left merge and spot fan-out risk.",
    ),
    "pd-dt": _g(
        "to_datetime + period('M') bilan oylik agregat qilasiz.",
        "to_datetime + period('M') билан ойлик агрегат қиласиз.",
        "Сделаете месячную агрегацию через to_datetime.",
        "You aggregate monthly with to_datetime + period.",
    ),
    "pd-eda": _g(
        "describe va value_counts bilan EDA boshlaysiz.",
        "describe ва value_counts билан EDA бошлайсиз.",
        "Начнёте EDA с describe и value_counts.",
        "You start EDA with describe and value_counts.",
    ),
    "py-mpl": _g(
        "Line chart bilan oylik trendni chizasiz.",
        "Line chart билан ойлик трендни чизасиз.",
        "Построите месячный тренд line chart-ом.",
        "You plot a monthly trend with a line chart.",
    ),
    "py-sns": _g(
        "Boxplot bilan outlier larni ko‘rasiz.",
        "Boxplot билан outlier ларни кўрасиз.",
        "Увидите выбросы на boxplot.",
        "You spot outliers with a boxplot.",
    ),
    "py-kpi": _g(
        "AOV/KPI ta’rifini hujjatlashtirib hisoblaysiz.",
        "AOV/KPI таърифини ҳужжатлаштириб ҳисоблайсиз.",
        "Задокументируете и посчитаете AOV/KPI.",
        "You define and compute documented AOV/KPIs.",
    ),
    "py-rfm": _g(
        "Recency (kun) ni hisoblab churn signalini topasiz.",
        "Recency (кун) ни ҳисоблаб churn сигналини топасиз.",
        "Посчитаете recency (дни) и сигнал churn.",
        "You compute recency days and a churn signal.",
    ),
    "py-final": _g(
        "Tozalash → KPI → vizual → tavsiya ketma-ketligini qo‘llaysiz.",
        "Тозалаш → KPI → визуал → тавсия кетма-кетлигини қўллайсиз.",
        "Примените цепочку: очистка → KPI → визуал → рекомендация.",
        "You apply clean → KPI → visual → recommendation.",
    ),
}
