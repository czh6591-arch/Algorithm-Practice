import json
from app.database import get_db

def init_data():
    db = get_db()
    
    if db.execute('SELECT COUNT(*) FROM problems').fetchone()[0] == 0:
        problems_data = [
            {
                'title': '两数之和',
                'difficulty': '简单',
                'description': '给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。',
                'input_format': '第一行输入整数 n，表示数组长度。第二行输入 n 个整数，表示数组元素。第三行输入目标值 target。',
                'output_format': '输出两个整数，表示满足条件的下标。',
                'sample_inputs': ['4\n2 7 11 15\n9', '3\n3 2 4\n6'],
                'sample_outputs': ['0 1', '1 2'],
                'constraints': '2 <= n <= 10^4\n-10^9 <= nums[i] <= 10^9\n-10^9 <= target <= 10^9',
                'max_time_complexity': 'O(n)',
                'max_space_complexity': 'O(n)',
                'test_cases': json.dumps([
                    {'input': '4\n2 7 11 15\n9', 'output': '0 1'},
                    {'input': '3\n3 2 4\n6', 'output': '1 2'},
                    {'input': '2\n1 3\n4', 'output': '0 1'},
                    {'input': '5\n-1 -2 -3 -4 -5\n-8', 'output': '2 4'},
                    {'input': '10000\n' + ' '.join(['1'] * 10000) + '\n2', 'output': '0 1'},
                    {'input': '9999\n' + ' '.join([str(i) for i in range(9999)]) + '\n19995', 'output': '9997 9998'}
                ])
            },
            {
                'title': '反转链表',
                'difficulty': '简单',
                'description': '给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。',
                'input_format': '第一行输入整数 n，表示链表节点数。第二行输入 n 个整数，表示链表各节点的值。',
                'output_format': '输出反转后的链表各节点值，用空格分隔。',
                'sample_inputs': ['5\n1 2 3 4 5', '2\n1 2'],
                'sample_outputs': ['5 4 3 2 1', '2 1'],
                'constraints': '1 <= n <= 5 * 10^4\n-5000 <= Node.val <= 5000',
                'max_time_complexity': 'O(n)',
                'max_space_complexity': 'O(1)',
                'test_cases': json.dumps([
                    {'input': '5\n1 2 3 4 5', 'output': '5 4 3 2 1'},
                    {'input': '2\n1 2', 'output': '2 1'},
                    {'input': '1\n5', 'output': '5'},
                    {'input': '3\n-1 0 1', 'output': '1 0 -1'},
                    {'input': '50000\n' + ' '.join([str(i) for i in range(50000)]) + '\n', 'output': ' '.join([str(i) for i in range(49999, -1, -1)])},
                    {'input': '49999\n' + ' '.join(['10'] * 49999) + '\n', 'output': ' '.join(['10'] * 49999)}
                ])
            },
            {
                'title': '有效的括号',
                'difficulty': '简单',
                'description': '给定一个只包括 ()，{}，[] 的字符串 s ，判断字符串是否有效。',
                'input_format': '输入一个字符串 s。',
                'output_format': '输出 true 或 false。',
                'sample_inputs': ['()', '()[]{}'],
                'sample_outputs': ['true', 'true'],
                'constraints': '1 <= s.length <= 10^4\ns 仅由括号 (){}[] 组成',
                'max_time_complexity': 'O(n)',
                'max_space_complexity': 'O(n)',
                'test_cases': json.dumps([
                    {'input': '()', 'output': 'true'},
                    {'input': '()[]{}', 'output': 'true'},
                    {'input': '(]', 'output': 'false'},
                    {'input': '([)]', 'output': 'false'},
                    {'input': '(' + ')' * 9999 + ')', 'output': 'true'},
                    {'input': '{' * 5000 + '}' * 5000, 'output': 'true'}
                ])
            },
            {
                'title': '最长回文子串',
                'difficulty': '中等',
                'description': '给你一个字符串 s，找到 s 中最长的回文子串。',
                'input_format': '输入一个字符串 s。',
                'output_format': '输出最长的回文子串。',
                'sample_inputs': ['babad', 'cbbd'],
                'sample_outputs': ['bab', 'bb'],
                'constraints': '1 <= s.length <= 1000\ns 仅由数字和英文字母组成',
                'time_complexity': 'O(n^2)',
                'space_complexity': 'O(1)',
                'max_time_complexity': 'O(n^2)',
                'max_space_complexity': 'O(1)',
                'test_cases': json.dumps([
                    {'input': 'babad', 'output': 'bab'},
                    {'input': 'cbbd', 'output': 'bb'},
                    {'input': 'a', 'output': 'a'},
                    {'input': 'ac', 'output': 'a'},
                    {'input': 'a' * 900 + 'bc' + 'a' * 900, 'output': 'a' * 900 + 'bc' + 'a' * 900},
                    {'input': 'abcdefghijklmnopqrstuvwxyz' * 38 + 'a', 'output': 'a'}
                ])
            },
            {
                'title': '合并区间',
                'difficulty': '中等',
                'description': '以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间。',
                'input_format': '第一行输入整数 n，表示区间数量。接下来 n 行，每行输入两个整数，表示区间的起始和结束。',
                'output_format': '输出合并后的区间，每行一个区间。',
                'sample_inputs': ['4\n1 3\n2 6\n8 10\n15 18', '2\n1 4\n4 5'],
                'sample_outputs': ['1 6\n8 10\n15 18', '1 5'],
                'constraints': '1 <= intervals.length <= 10^4\n0 <= starti <= endi <= 10^4',
                'time_complexity': 'O(n log n)',
                'space_complexity': 'O(n)',
                'max_time_complexity': 'O(n log n)',
                'max_space_complexity': 'O(n)',
                'test_cases': json.dumps([
                    {'input': '4\n1 3\n2 6\n8 10\n15 18', 'output': '1 6\n8 10\n15 18'},
                    {'input': '2\n1 4\n4 5', 'output': '1 5'},
                    {'input': '1\n1 1', 'output': '1 1'},
                    {'input': '3\n1 2\n3 5\n6 7', 'output': '1 2\n3 5\n6 7'},
                    {'input': '9000\n' + '\n'.join([f'{i} {i+1}' for i in range(9000)]) + '\n', 'output': '0 9000'},
                    {'input': '8999\n' + '\n'.join([f'{i*2} {i*2+1}' for i in range(8999)]) + '\n', 'output': '\n'.join([f'{i*2} {i*2+1}' for i in range(8999)])}
                ])
            },
            {
                'title': '二叉树的层序遍历',
                'difficulty': '中等',
                'description': '给你二叉树的根节点 root，返回其节点值的层序遍历。（即逐层地，从左到右访问所有节点）。',
                'input_format': '输入二叉树的层序表示，空节点用 null 表示。',
                'output_format': '输出层序遍历的结果，每一层用空格分隔。',
                'sample_inputs': ['3 9 20 null null 15 7', '1'],
                'sample_outputs': ['3\n9 20\n15 7', '1'],
                'constraints': '树中节点数目在范围 [0, 2000] 内\n-1000 <= Node.val <= 1000',
                'time_complexity': 'O(n)',
                'space_complexity': 'O(n)',
                'max_time_complexity': 'O(n)',
                'max_space_complexity': 'O(n)',
                'test_cases': json.dumps([
                    {'input': '3 9 20 null null 15 7', 'output': '3\n9 20\n15 7'},
                    {'input': '1', 'output': '1'},
                    {'input': '', 'output': ''},
                    {'input': '1 2 null 3 null 4', 'output': '1\n2\n3\n4'},
                    {'input': '1 ' + ' '.join(['2'] * 1999), 'output': '1\n' + ' '.join(['2'] * 1999)},
                    {'input': '1 2 3 4 5 6 7 ' + ' '.join(['null'] * 14) + '8', 'output': '1\n2 3\n4 5 6 7\n8'}
                ])
            },
            {
                'title': '编辑距离',
                'difficulty': '困难',
                'description': '给你两个单词 word1 和 word2，请返回将 word1 转换成 word2 所使用的最少操作数。',
                'input_format': '第一行输入 word1，第二行输入 word2。',
                'output_format': '输出最少操作数。',
                'sample_inputs': ['horse\nros', 'intention\nexecution'],
                'sample_outputs': ['3', '5'],
                'constraints': '0 <= word1.length, word2.length <= 500\nword1 和 word2 由小写英文字母组成',
                'time_complexity': 'O(m * n)',
                'space_complexity': 'O(m * n)',
                'max_time_complexity': 'O(m * n)',
                'max_space_complexity': 'O(m * n)',
                'test_cases': json.dumps([
                    {'input': 'horse\nros', 'output': '3'},
                    {'input': 'intention\nexecution', 'output': '5'},
                    {'input': 'a\nb', 'output': '1'},
                    {'input': '\na', 'output': '1'},
                    {'input': 'a' * 400 + '\nb' * 400, 'output': '400'},
                    {'input': 'abcde' * 100 + '\nabced' * 100, 'output': '100'}
                ])
            },
            {
                'title': '最长递增子序列',
                'difficulty': '困难',
                'description': '给你一个整数数组 nums，找到其中最长严格递增子序列的长度。',
                'input_format': '第一行输入整数 n，表示数组长度。第二行输入 n 个整数。',
                'output_format': '输出最长递增子序列的长度。',
                'sample_inputs': ['8\n10 9 2 5 3 7 101 18', '4\n0 1 0 3 2 3'],
                'sample_outputs': ['4', '4'],
                'constraints': '1 <= n <= 2500\n-10^4 <= nums[i] <= 10^4',
                'time_complexity': 'O(n log n)',
                'space_complexity': 'O(n)',
                'max_time_complexity': 'O(n log n)',
                'max_space_complexity': 'O(n)',
                'test_cases': json.dumps([
                    {'input': '8\n10 9 2 5 3 7 101 18', 'output': '4'},
                    {'input': '4\n0 1 0 3 2 3', 'output': '4'},
                    {'input': '1\n1', 'output': '1'},
                    {'input': '3\n3 2 1', 'output': '1'},
                    {'input': '2400\n' + ' '.join([str(i) for i in range(2400)]) + '\n', 'output': '2400'},
                    {'input': '2399\n' + ' '.join([str(2399-i) for i in range(2399)]) + '\n', 'output': '1'}
                ])
            },
            {
                'title': '最大矩形',
                'difficulty': '困难',
                'description': '给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。',
                'input_format': '第一行输入行数 m 和列数 n。接下来 m 行，每行输入 n 个数字（0 或 1）。',
                'output_format': '输出最大矩形的面积。',
                'sample_inputs': ['3 3\n1 0 1\n0 1 1\n1 1 1', '1 1\n0'],
                'sample_outputs': ['4', '0'],
                'constraints': 'm == matrix.length\nn == matrix[0].length\n1 <= m, n <= 200\nmatrix[i][j] 为 0 或 1',
                'time_complexity': 'O(m * n)',
                'space_complexity': 'O(n)',
                'max_time_complexity': 'O(m * n)',
                'max_space_complexity': 'O(n)',
                'test_cases': json.dumps([
                    {'input': '3 3\n1 0 1\n0 1 1\n1 1 1', 'output': '4'},
                    {'input': '1 1\n0', 'output': '0'},
                    {'input': '1 3\n1 1 1', 'output': '3'},
                    {'input': '2 2\n1 1\n1 1', 'output': '4'},
                    {'input': '190 190\n' + '\n'.join(['1' * 190 for _ in range(190)]) + '\n', 'output': '36100'},
                    {'input': '189 189\n' + '\n'.join(['1' * i + '0' * (189-i) for i in range(189)]) + '\n', 'output': '9075'}
                ])
            }
        ]
        
        for problem in problems_data:
            db.execute('''
                INSERT INTO problems (title, difficulty, description, input_format, output_format,
                                   sample_inputs, sample_outputs, constraints, time_complexity,
                                   space_complexity, max_time_complexity, max_space_complexity, test_cases)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                problem['title'],
                problem['difficulty'],
                problem['description'],
                problem['input_format'],
                problem['output_format'],
                json.dumps(problem['sample_inputs']),
                json.dumps(problem['sample_outputs']),
                problem['constraints'],
                problem.get('time_complexity'),
                problem.get('space_complexity'),
                problem['max_time_complexity'],
                problem['max_space_complexity'],
                problem['test_cases']
            ))
    
    if db.execute('SELECT COUNT(*) FROM tutorials').fetchone()[0] == 0:
        tutorials_data = [
            {'category': '排序算法', 'title': '快速排序', 'content': '快速排序是一种分治算法。它的基本思想是：选择一个基准元素，将数组分成两部分，使得左边的元素都小于等于基准元素，右边的元素都大于等于基准元素，然后递归地对左右两部分进行排序。', 'video_url': 'https://www.youtube.com/embed/PgBzjlCcFvc'},
            {'category': '排序算法', 'title': '归并排序', 'content': '归并排序是一种分治算法。它将数组分成两半，分别对每一半进行排序，然后将排序好的两半合并起来。归并排序的时间复杂度为O(n log n)，空间复杂度为O(n)。', 'video_url': 'https://www.youtube.com/embed/JSceec-wEyw'},
            {'category': '排序算法', 'title': '堆排序', 'content': '堆排序利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。', 'video_url': 'https://www.youtube.com/embed/MtQL_ll5KhQ'},
            {'category': '排序算法', 'title': '插入排序', 'content': '插入排序是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。', 'video_url': 'https://www.youtube.com/embed/OGzPmgsI-pQ'},
            {'category': '数据结构', 'title': '二叉搜索树', 'content': '二叉搜索树（BST）是一种二叉树数据结构，其中每个节点的左子树只包含小于该节点值的节点，右子树只包含大于该节点值的节点。BST支持O(log n)时间复杂度的插入、删除和查找操作。', 'video_url': 'https://www.youtube.com/embed/UScZOfvIFe8'},
            {'category': '数据结构', 'title': '哈希表', 'content': '哈希表是一种通过哈希函数将键映射到值的数据结构。它提供平均O(1)时间复杂度的插入、删除和查找操作。哈希冲突是哈希表设计中的一个重要问题。', 'video_url': 'https://www.youtube.com/embed/54iv1si4YCM'},
            {'category': '数据结构', 'title': '图的表示', 'content': '图可以用邻接矩阵或邻接表来表示。邻接矩阵适合稠密图，而邻接表适合稀疏图。图的遍历算法包括深度优先搜索（DFS）和广度优先搜索（BFS）。', 'video_url': 'https://www.youtube.com/embed/bIA8HEEUxZI'},
            {'category': '数据结构', 'title': '栈和队列', 'content': '栈是一种后进先出（LIFO）的数据结构，队列是一种先进先出（FIFO）的数据结构。栈常用于表达式求值、括号匹配等问题，队列常用于BFS算法中。', 'video_url': 'https://www.youtube.com/embed/9I82M5u3WK4'},
            {'category': '进阶算法', 'title': '动态规划入门', 'content': '动态规划是一种将复杂问题分解为子问题来求解的方法。它适用于具有最优子结构和重叠子问题特性的问题。动态规划通常使用表格来存储子问题的解。', 'video_url': 'https://www.youtube.com/embed/oBt53YbR9Kk'},
            {'category': '进阶算法', 'title': '贪心算法', 'content': '贪心算法在每一步都选择当前最优的选择，希望通过局部最优达到全局最优。贪心算法适用于具有贪心选择性质的问题，如活动选择、哈夫曼编码等。', 'video_url': 'https://www.youtube.com/embed/HzeK7g8cD0Y'},
            {'category': '进阶算法', 'title': '图论算法', 'content': '图论算法包括最短路径算法（如Dijkstra、Floyd-Warshall）、最小生成树算法（如Prim、Kruskal）、网络流算法等。这些算法在网络设计、路径规划等领域有广泛应用。', 'video_url': 'https://www.youtube.com/embed/tWVWeAqZ0WU'},
            {'category': '进阶算法', 'title': '字符串匹配', 'content': '字符串匹配算法用于在文本中查找模式串的出现位置。常见的算法包括暴力匹配、KMP算法、Boyer-Moore算法等。KMP算法通过预处理模式串来避免不必要的比较。', 'video_url': 'https://www.youtube.com/embed/GTJr8OvyEVQ'}
        ]
        
        for tutorial in tutorials_data:
            db.execute('INSERT INTO tutorials (category, title, content, video_url) VALUES (?, ?, ?, ?)',
                      (tutorial['category'], tutorial['title'], tutorial['content'], tutorial['video_url']))
    
    db.commit()
    db.close()

if __name__ == "__main__":
    init_data()