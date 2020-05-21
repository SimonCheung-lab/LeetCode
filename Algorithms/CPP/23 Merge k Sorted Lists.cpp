/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    // merge k is no different with merge two
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.size() == 0) {
            return NULL;
        }

        return merge(lists, 0, lists.size() - 1);
    }

    ListNode* merge(vector<ListNode*>& lists, int left, int right) {
        if (left == right) {
            return lists[left];
        }

        int mid = (left + right) / 2;
        ListNode* leftList = merge(lists, left, mid);
        ListNode* rightList = merge(lists, mid + 1, right);
        return mergeTwo(leftList, rightList);
    }

    ListNode* mergeTwo(ListNode* left, ListNode* right) {
        ListNode* head, *p;
        head = p = NULL;
        while (left || right) {
            if (left == NULL || (right && right->val <= left->val)) {
                if (p == NULL){
                    head = p = right;
                }
                else {
                    p->next = right;
                    p = p->next;
                }
                right = right->next;
            }
            else {
                if (p == NULL) {
                    head = p = left;
                }
                else {
                    p->next = left;
                    p = p->next;
                }
                left = left->next;
            }
        }

        return head;
    }
};
