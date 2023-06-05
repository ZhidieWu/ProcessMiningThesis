from pm4py.visualization.bpmn import visualizer as bpmn_visualizer
from pm4py.visualization.petri_net import visualizer as petri_visualizer
import pm4py
from pm4py.algo.discovery.footprints import algorithm as footprints_discovery





bpmn_graph = pm4py.read_bpmn("Data/testPart1.bpmn")
bpmn_visualization = bpmn_visualizer.apply(bpmn_graph)
bpmn_visualizer.view(bpmn_visualization)
net, im, fm = pm4py.convert_to_petri_net(bpmn_graph)
petri_visualization = petri_visualizer.apply(net)
bpmn_visualizer.view(petri_visualization)
# 导出Petri网为PNML文件
pnml_path = "Data/testPart1.pnml"
pm4py.write_pnml(net, im, fm, pnml_path)
log = pm4py.play_out(net, im, fm)

fp_net = footprints_discovery.apply(net, im, fm)
print(fp_net)

print("###################bpmn##################")
ft_print = footprints_discovery.apply(bpmn_graph,im,fm)
nodes,edge=pm4py.objects.bpmn.util.sorting.get_sorted_nodes_edges(bpmn_graph)
#ft_print = footprints_discovery.trace_by_trace.apply(bpmn_log)
print(nodes)
