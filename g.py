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

#import org.gephi.io.importer.api.EdgeDirectionDefault

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

def main():
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
    
if __name__=='__main__':main()
