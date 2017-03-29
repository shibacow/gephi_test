#import org.gephi.profrom  import ProjectController
#ProjectController().newProject()
#workspace = ProjectController().getCurrentWorkspace()
#print workspace

import org.gephi.project.api as project
from org.openide.util import Lookup
import org.gephi.graph.api as graph
import org.gephi.preview.api as preview
import org.gephi.io.importer.api as importer
import org.gephi.filters.api as filters
import org.gephi.appearance.api as appearance
from java.io import File
import org.gephi.io.processor.plugin as processor
import org.gephi.filters.plugin.graph.DegreeRangeBuilder as degree_range_builder
import sys
import org.gephi.layout.plugin.force as force
import org.gephi.statistics.plugin as statistics
#import org.gephi.io.importer.api.EdgeDirectionDefault
from glob import glob

def ProjectController(lookup):
    return lookup(project.ProjectController)
def GraphController(lookup):
    return lookup(graph.GraphController)
def PreviewController(lookup):
    return lookup(preview.PreviewController)
def ImportController(lookup):
    return lookup(importer.ImportController)
def FilterController(lookup):
    return lookup(filters.FilterController)
def AppearanceController(lookup):
    return lookup(appearance.AppearanceController)

def headless():
    lookup = Lookup.getDefault().lookup
    pc =ProjectController(lookup)
    pc.newProject()
    workspace = pc.getCurrentWorkspace()
    graph_model = GraphController(lookup).getGraphModel()
    print(graph_model)
    preview_model = PreviewController(lookup)
    print(preview_model)
    import_controller = ImportController(lookup)
    print(import_controller)
    filter_controller = FilterController(lookup)
    print(filter_controller)
    appearance_controller = AppearanceController(lookup)
    print(appearance_controller)
    appearance_model = appearance_controller.getModel()
    print(appearance_model)
    try:
        container = import_controller.importFile(File('resources/polblogs.gml'))
        container.getLoader().setEdgeDefault(importer.EdgeDirectionDefault.DIRECTED)
    except Exception,err:
        print(err)
    import_controller.process(container,processor.DefaultProcessor(),workspace)
    graph = graph_model.getDirectedGraph()
    print(graph.getNodeCount())
    print(graph.getEdgeCount())
    degreefilter=degree_range_builder.DegreeRangeFilter()
    degreefilter.init(graph)
    degreefilter.setRange(filters.Range(30,sys.maxint))
    query = FilterController(lookup).createQuery(degreefilter)
    view = FilterController(lookup).filter(query)
    graph_model.setVisibleView(view)
    graph_visible = graph_model.getUndirectedGraphVisible()
    print(graph_visible.getNodeCount())
    print(graph_visible.getEdgeCount())
    layout = force.yifanHu.YifanHuLayout(None,force.StepDisplacement(1))
    layout.setGraphModel(graph_model)
    layout.resetPropertiesValues()
    layout.setOptimalDistance(200.0)
    layout.initAlgo()
    for i in  range(100):
        v=layout.getAverageEdgeLength(graph)
        print("i={} ratio={}".format(i,v))
        if layout.canAlgo():
            layout.goAlgo()
        else:
            break
    layout.endAlgo()

    distance = statistics.GraphDistance()
    distance.setDirected(True)
    distance.execute(graph_model)

    #//Rank color by Degree
    #System.out.println("start color by Degree");
    #Function degreeRanking = appearanceModel.getNodeFunction(graph, AppearanceModel.GraphFunction.NODE_DEGREE, RankingElementColorTransformer.class);
    #RankingElementColorTransformer degreeTransformer = (RankingElementColorTransformer) degreeRanking.getTransformer();
    #degreeTransformer.setColors(new Color[]{new Color(0xFEF0D9), new Color(0xB30000)});
    #degreeTransformer.setColorPositions(new float[]{0f, 1f});
    #appearanceController.transform(degreeRanking);
    #System.out.println("end color by Degree");

def main():
    headless()
if __name__=='__main__':main()
