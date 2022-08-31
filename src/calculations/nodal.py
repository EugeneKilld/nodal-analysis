from shapely.geometry import LineString

from src.models.models import NodalCalcDecision


def calc_nodal(vlp: dict, ipr: dict):
    """
    Расчёт точки пересечения VLP vs IPR

    Parameters
    ----------
    vlp : dict
        Словарь, содержащий VLP
    ipr : dict
        Словарь, содержащий IPR
    """
    # Можно использовать numpy или библиотеку Shapely, LineString intersection
    vlpLine = LineString(zip(vlp["p_wf"], vlp["q_liq"]))
    iprLine = LineString(zip(ipr["p_wf"], ipr["q_liq"]))
    points = vlpLine.intersection(iprLine)
    result = NodalCalcDecision(p_wf=points.x, q_liq=points.y).dict()

    return [result]

