'''
     Input: Genomes P and Q.
          (+1 +2 +3 +4 +5 +6)
          (+1 -3 -6 -5)(+2 -4)
     Output: The 2-break distance d(P, Q).
          3
     Logic:
        Think of the blocks 1,2,3,4,5,6 as having two ends, plus and minus. "+1" means the first block is in positive orientation, 
        you could think of the minus end on the left and the plus end on the right. If two blocks are arranged in order 
        with + orientation as they are in the first line of input, then the plus end of 1 is connected to the minus end of 2. 
        Of course the minus end of 1 is connected to the plus end of 1 but were going to forget about that for this problem, 
        treat the two ends as separate nodes. So the (undirected) edges for the first line of input are:
           1+,2-; 2+,3-; 3+,4-; 4+,5-; 5+,6-;
        and then circularize it by adding 6+,1-
        The second line of input has two groups:
          1+,3+; 3-,6+; 6-,5+; 5-,1-;
          2+,4+; 4-,2-;
        Now add ALL of those edges to a single graph and find cycles, there should be 3:
          1+,2-,4-,3+,back to 1+
          2+,3-,6+,1-,5-,4+, back to 2+
          5+,6-, back to 5+
        and so d(P,Q) = blocks(P,Q) - cycle(P,Q)
         = 6 - 3
         = 3
        Blue edges are for P and red edges are for Q.
        Total Blocks = 6
'''

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using CRM.FelonAudit.Activities;
using Microsoft.Xrm.Sdk.Client;
using System.Configuration;
using System.ServiceModel.Description;
using Microsoft.Crm.Sdk.Messages;
using System.Diagnostics;
using System.IO;
using System.Collections;
using System.Text.RegularExpressions;

namespace CRM.FelonAudit.Test
{
    class Program
    {
        static void Main(string[] args)
        {
            Program.TwoBreakDistance();
         }

        #region "TwoBreakDistance()"
        static ArrayList nodes = new ArrayList();
        public static void TwoBreakDistance()
        {
            DateTime dt0 = DateTime.Now;
            dt0.ToLongTimeString();
            string line = "";
            int count = 0;
            StreamReader file = new StreamReader(@"C:\Users\kaderm\Downloads\w_8_3_dataset1.txt");
            
            int countblocks = 0;

            while ((line = file.ReadLine()) != null)
            {
                if (count == 0)
                {
                    countblocks = MergeOpenClose(line);
                }
                else if (count == 1)
                {
                    MergeOpenClose(line);
                }
                else
                    break;
                count++;
            }
            bool[] bnodes = new bool[nodes.Count];
       
            System.IO.File.WriteAllText(@"C:\Users\kaderm\Downloads\result.txt", string.Empty);
            StreamWriter writer = new StreamWriter(@"C:\Users\kaderm\Downloads\result.txt", true);
            for (int i = 0; i < nodes.Count; i++)
            {
                writer.WriteLine(nodes[i]);
            }
            writer.WriteLine("Total Blocks = " + countblocks);
            string[] node;
            ArrayList cycles = new ArrayList();
            for (int i = 0; i < nodes.Count-1; i++)
            {
                if (!bnodes[i])
                {
                    node = (nodes[i].ToString()).Split(' ');
                    string snode=node[0];
                    string enode=node[1];
                    string cycle = nodes[i].ToString();
                    for (int j = 0; j < nodes.Count; j++)
                    {
                        string[] cnode = (nodes[j].ToString()).Split(' ');
                        if (i != j && !bnodes[j])
                        {
                            int tj = j;
                            if (snode == cnode[0])
                            {
                                cycle = cnode[1]+ " " +cycle;
                                snode = cnode[1];
                                j = -1;
                            }
                            else if (snode == cnode[1])
                            {
                                cycle = cnode[0] + " " + cycle;
                                snode = cnode[0];
                                j=-1;
                            }
                            else if (enode == cnode[0])
                            {
                                cycle = cycle + " " + cnode[1];
                                enode = cnode[1];
                                j=-1;
                            }
                            else if (enode == cnode[1])
                            {
                                cycle = cycle + " " + cnode[0];
                                enode = cnode[0];
                                j = -1;
                            }
                            if (j == -1)
                            {
                                //writer.WriteLine(nodes[i]);
                                bnodes[i] = true;
                                bnodes[tj] = true;
                            }
                        }
                    }
                    cycles.Add(cycle);
                }
            }

            writer.WriteLine("Total Cycles = " + cycles.Count);
            writer.WriteLine("2 Break Distance = " + (countblocks-cycles.Count));
            for (int i = 0; i < cycles.Count; i++)
            {
                writer.WriteLine(cycles[i]);
            }
            writer.Close();

            DateTime dt1 = DateTime.Now;
            Console.WriteLine("Done - " + (dt0 - dt1).ToString());
            Console.ReadLine();
        }

        private static int MergeOpenClose(string line)
        {
            string pattern = @"\(.*?\)";
            //string[] genomes = Regex.Split(line, pattern);
            var matches = Regex.Matches(line, pattern);
            string node = "";
            string tend = "";
            string end = "";
            string start = "";
            int totblocks = 0;
            foreach (Match mat in matches)
            {
                string[] genome = (RemoveOpenClose(mat.Value)).Split(' ');
                for (int j = 0; j < genome.Length-1; j++)
                {
                    start = genome[j];
                    end = genome[j+1];
                    if (end.Contains("+"))
                    {
                        tend = end.Replace("+", "-");
                    }
                    else if (end.Contains("-"))
                    {
                        tend = end.Replace("-", "+");
                    }
                    node = start + " " + tend;
                    nodes.Add(node);
                    totblocks++;
                    //start = ConvertPlusMinus(tend);
                }
                start = genome[genome.Length-1];
                end = genome[0];
                if (end.Contains("+"))
                {
                    tend = end.Replace("+", "-");
                }
                else if (end.Contains("-"))
                {
                    tend = end.Replace("-", "+");
                }
                node = start + " " + tend;
                nodes.Add(node);
                totblocks++;
            }
            return totblocks;
        }

        private static string ConvertPlusMinus(string genome)
        {
            string start = "";
            if (genome.Contains("+"))
            {
                start = genome.Replace("+", "-");
            }
            else if (genome.Contains("-"))
            {
                start = genome.Replace("-", "+");
            }
            return start;
        }

        private static string RemoveOpenClose(string genomes)
        {
            string in_genomes = "";
            if (genomes.Length > 0)
            {
                in_genomes = genomes;
                in_genomes = in_genomes.Replace(")", "");
                in_genomes = in_genomes.Replace("(", "");
            }
            return in_genomes;
        }
        #endregion "TwoBreakDistance()"

    }
}
