#include <float.h>
#include <fstream>
#include <iostream>
#include <math.h>
#include <string>
#include <vector>

/*---------------- Data Structure ----------------*/
struct Coordinate
{
    int iX;
    int iY;
};

struct CostValue
{
    float fValue;
    float hValue;
    float gValue;
};

struct CellDetail
{
    Coordinate currentPosition;
    Coordinate parentPosition;
    CostValue cost;
};
/*--------------------------------------------------*/

char *inFileName;
char *outFileName;

std::ostream &operator<<(std::ostream &outStream, const Coordinate &obj)
{
    outStream << '(' << obj.iX << ", " << obj.iY << ')';
    return outStream;
}

std::istream &operator>>(std::istream &inStream, Coordinate &obj)
{
    inStream >> obj.iX >> obj.iY;
    return inStream;
}

bool operator==(const Coordinate &coor_A, const Coordinate &coor_B)
{
    if (coor_A.iX == coor_B.iX && coor_A.iY == coor_B.iY)
        return true;
    else
        return false;
}

template <class T> void clean_2D_Data(T **&data, int Length_Matrix)
{
    for (int i = 0; i < Length_Matrix; i++)
        delete[] data[i];
}

int read_Data_From_File(int &Length_Matrix, Coordinate &start_point,
                        Coordinate &end_point, int **&Graph)
{
    std::fstream inFile(inFileName, std::ios::in);

    if (!inFile.is_open())
    {
        std::cout << "can not read data from file" << std::endl;
        return 0;
    }

    inFile >> Length_Matrix;
    inFile >> start_point >> end_point;

    // create 2D Graph (N*N) -----------------
    Graph = new int *[Length_Matrix];

    for (int i = 0; i < Length_Matrix; i++)
    {
        Graph[i] = new int[Length_Matrix];
    }

    for (int i = 0; i < Length_Matrix; i++)
        for (int j = 0; j < Length_Matrix; j++)
            inFile >> Graph[i][j];

    inFile.close();

    return 1;
}

bool is_Valid(const Coordinate &obj, int Length_Matrix)
{
    if ((obj.iX >= 0 && obj.iX < Length_Matrix) &&
        (obj.iY >= 0 && obj.iY < Length_Matrix))
        return true;
    else
        return false;
}

bool is_Unblocked(const Coordinate &obj, int **Graph)
{
    int i = obj.iX;
    int j = obj.iY;

    if (Graph[i][j] == 0)
        return true;
    else
        return false;
}

float calculate_hValue(const Coordinate &A, const Coordinate &B)
{
    int deltaX = B.iX - A.iX;
    int deltaY = B.iY - A.iY;

    return sqrt(float(deltaX * deltaX + deltaY * deltaY));
}

void outputFile(const std::vector<Coordinate> &Path, int **Graph,
                int Length_Matrix)
{
    // init output Graph
    char **outGraph = new char *[Length_Matrix];
    for (int i = 0; i < Length_Matrix; i++)
        outGraph[i] = new char[Length_Matrix];

    // modify output graph
    for (int i = 0; i < Length_Matrix; i++)
        for (int j = 0; j < Length_Matrix; j++)
        {
            if (Graph[i][j] == 0)
                outGraph[i][j] = '_';
            else
                outGraph[i][j] = 'o';
        }

    outGraph[Path[0].iX][Path[0].iY] = 'G';
    outGraph[Path[Path.size() - 1].iX][Path[Path.size() - 1].iY] = 'S';

    for (int i = 1; i < Path.size() - 1; i++)
        outGraph[Path[i].iX][Path[i].iY] = 'x';

    std::fstream outFile(outFileName, std::ios::out);

    // print data to file
    outFile << Path.size() << std::endl;

    for (int i = Path.size() - 1; i >= 0; i--)
        outFile << Path[i] << "  ";
    outFile << std::endl;

    for (int i = 0; i < Length_Matrix; i++)
    {
        for (int j = 0; j < Length_Matrix; j++)
        {
            outFile << ' ' << outGraph[i][j];
        }
        outFile << std::endl;
    }

    outFile.close();

    // clean memory
    clean_2D_Data<char>(outGraph, Length_Matrix);
}

void trace_Path(CellDetail **&Cell, const Coordinate &end_point,
                const Coordinate &start_point, int **Graph, int Length_Matrix)
{
    // create a Path with vector
    std::vector<Coordinate> Path;
    Path.resize(0);

    // push destiny to Path
    Path.push_back(end_point);

    // create temp variable to store parent position
    Coordinate temp = end_point;

    // trace path till find start_point
    while (!(temp == start_point))
    {
        int i = Cell[temp.iX][temp.iY].parentPosition.iX;
        int j = Cell[temp.iX][temp.iY].parentPosition.iY;

        temp.iX = i;
        temp.iY = j;

        Path.push_back(temp);
    }

    outputFile(Path, Graph, Length_Matrix);
}

int create_Successor(CellDetail **Cell, std::vector<CellDetail> &opened_Cell,
                     const Coordinate &end_point, const Coordinate &start_point,
                     const Coordinate &current, int deltaX, int deltaY,
                     int Length_Matrix, int **Graph, int **closed_Cell)
{
    Coordinate successor;
    successor.iX = current.iX + deltaX;
    successor.iY = current.iY + deltaY;

    // check if this successor is valid or not
    if (is_Valid(successor, Length_Matrix) == true)
    {
        int i = successor.iX;
        int j = successor.iY;
        // if this successor is destiny
        if (i == end_point.iX && j == end_point.iY)
        {
            Cell[i][j].parentPosition.iX = current.iX;
            Cell[i][j].parentPosition.iY = current.iY;

            trace_Path(Cell, end_point, start_point, Graph, Length_Matrix);
            return 1;
        }
        // if this successor is closed or blocked
        else if (is_Unblocked(successor, Graph) == false ||
                 closed_Cell[i][j] == true)
            return -1;
        // diffrent case
        else
        {
            float gNewValue = Cell[current.iX][current.iY].cost.gValue + 1;
            float hNewValue = calculate_hValue(successor, end_point);
            float fNewValue = gNewValue + hNewValue;

            /* if it isn't in open cell, add it to open cell
                                 OR
               if it is in open cell, check if its old fValue
               is greatter fNewValue or not*/
            if (Cell[i][j].cost.fValue == FLT_MAX ||
                Cell[i][j].cost.fValue > fNewValue)
            {
                Cell[i][j].cost.fValue = fNewValue;
                Cell[i][j].cost.gValue = gNewValue;
                Cell[i][j].cost.hValue = hNewValue;
                Cell[i][j].parentPosition.iX = current.iX;
                Cell[i][j].parentPosition.iY = current.iY;

                // find suitable position to insert
                int pos = 0;

                while (pos < opened_Cell.size() &&
                       opened_Cell[pos].cost.fValue <= fNewValue)
                    pos += 1;

                if (pos == opened_Cell.size())
                    opened_Cell.push_back(Cell[i][j]);
                else
                    opened_Cell.insert(opened_Cell.begin() + pos, Cell[i][j]);
            }
        }
    }

    return -1;
}

int A_Start_Search(int **Graph, const Coordinate &start_point,
                   const Coordinate &end_point, const int Length_Matrix)
{
    // check if start point is valid or not
    if (is_Valid(start_point, Length_Matrix) == false)
    {
        std::cout << "start point is invalid" << std::endl;
        return 0;
    }

    // check if end point is valid or not
    if (is_Valid(end_point, Length_Matrix) == false)
    {
        std::cout << "end point is invalid" << std::endl;
        return 0;
    }

    // check if start point or end point is blocked or not
    if (is_Unblocked(start_point, Graph) == false ||
        is_Unblocked(end_point, Graph) == false)
    {
        std::cout << "start point or end point was blocked" << std::endl;
        return 0;
    }

    // check if start point is end point or not
    if (start_point == end_point)
    {
        std::cout << "start point is already end point" << std::endl;
        return 0;
    }

    // init cell detail matrix
    CellDetail **Cell = new CellDetail *[Length_Matrix];
    for (int i = 0; i < Length_Matrix; i++)
        Cell[i] = new CellDetail[Length_Matrix];

    for (int i = 0; i < Length_Matrix; i++)
        for (int j = 0; j < Length_Matrix; j++)
        {
            Cell[i][j].currentPosition.iX = i;
            Cell[i][j].currentPosition.iY = j;

            Cell[i][j].parentPosition.iX = -1;
            Cell[i][j].parentPosition.iY = -1;

            Cell[i][j].cost.fValue = FLT_MAX;
            Cell[i][j].cost.hValue = FLT_MAX;
            Cell[i][j].cost.gValue = FLT_MAX;
        }

    // init closed cell matrix
    int **closed_Cell = new int *[Length_Matrix];
    for (int i = 0; i < Length_Matrix; i++)
        closed_Cell[i] = new int[Length_Matrix];

    for (int i = 0; i < Length_Matrix; i++)
        for (int j = 0; j < Length_Matrix; j++)
            closed_Cell[i][j] = false;

    // init open list
    std::vector<CellDetail> opened_Cell;
    opened_Cell.resize(0);

    // add source cell to open cell list
    Cell[start_point.iX][start_point.iY].cost.fValue = 0.0;
    Cell[start_point.iX][start_point.iY].cost.hValue = 0.0;
    Cell[start_point.iX][start_point.iY].cost.gValue = 0.0;

    opened_Cell.push_back(Cell[start_point.iX][start_point.iY]);

    int sign; /* 1 if found destiny
                 -1 if its invalid position*/

    while (!opened_Cell.empty())
    {
        CellDetail tempCell = opened_Cell[0];
        opened_Cell.erase(opened_Cell.begin());

        Coordinate k = tempCell.currentPosition;
        closed_Cell[k.iX][k.iY] = true;

        // Generating all the 8 successor of this cell

        /*WEST-NORTH*/
        sign = create_Successor(Cell, opened_Cell, end_point, start_point, k,
                                -1, -1, Length_Matrix, Graph, closed_Cell);
        if (sign == 1)
            break;

        /*NORTH*/
        sign = create_Successor(Cell, opened_Cell, end_point, start_point, k,
                                -1, 0, Length_Matrix, Graph, closed_Cell);
        if (sign == 1)
            break;

        /*EAST-NORTH*/
        sign = create_Successor(Cell, opened_Cell, end_point, start_point, k,
                                -1, 1, Length_Matrix, Graph, closed_Cell);
        if (sign == 1)
            break;

        /*EAST*/
        sign = create_Successor(Cell, opened_Cell, end_point, start_point, k, 0,
                                1, Length_Matrix, Graph, closed_Cell);
        if (sign == 1)
            break;

        /*EAST-SOUTH*/
        sign = create_Successor(Cell, opened_Cell, end_point, start_point, k, 1,
                                1, Length_Matrix, Graph, closed_Cell);
        if (sign == 1)
            break;

        /*SOUTH*/
        sign = create_Successor(Cell, opened_Cell, end_point, start_point, k, 1,
                                0, Length_Matrix, Graph, closed_Cell);
        if (sign == 1)
            break;

        /*WEST-SOUTH*/
        sign = create_Successor(Cell, opened_Cell, end_point, start_point, k, 1,
                                -1, Length_Matrix, Graph, closed_Cell);
        if (sign == 1)
            break;

        /*WEST*/
        sign = create_Successor(Cell, opened_Cell, end_point, start_point, k, 0,
                                -1, Length_Matrix, Graph, closed_Cell);
        if (sign == 1)
            break;
    }

    // clear memory
    clean_2D_Data<CellDetail>(Cell, Length_Matrix);
    clean_2D_Data<int>(closed_Cell, Length_Matrix);

    // end program if find path success
    if (sign == 1)
        return 1;

    // can not find path
    std::fstream outFile(outFileName, std::ios::out);
    outFile << -1 << std::endl;
    outFile.close();

    return 0;
}

int main(int argc, char **argv)
{
    if (argc != 3)
    {
        std::cout << "usage : <program name> <input file> <output file>"
                  << std::endl;
        return 0;
    }

    int Length_Matrix;
    int **Graph;

    Coordinate start_point;
    Coordinate end_point;

    inFileName = argv[1];
    outFileName = argv[2];

    int returnValue =
        read_Data_From_File(Length_Matrix, start_point, end_point, Graph);

    if (returnValue == 0)
        return 0;

    A_Start_Search(Graph, start_point, end_point, Length_Matrix);

    // clean memory
    clean_2D_Data<int>(Graph, Length_Matrix);

    return 1;
}
