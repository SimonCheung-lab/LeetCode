/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
    if(NULL == l1){
        return l2;
    }
    if(NULL == l2){
        return l1;
    }
    struct ListNode *head, *p1, *p2, *p;
    int flag = 0;
    p1 = l1, p2 = l2;
    if(p1->val < p2->val){
        head = p1;
        p1 = p1->next;
        flag = 1;
    }
    else{
        head = p2;
        p2 = p2->next;
        flag = 2;
    }
    p = head;
    while(p1 && p2){
        if(flag == 1){
            while(p1 && (p1->val <= p2->val)){
                p1 = p1->next;
                p = p->next;
            }
            if(!p1 || !p2){
                break;
            }
            p->next = p2;
            p2 = p2->next;
            p = p->next;
            flag = 2;
        }
        else{
            while(p2 && (p2->val <= p1->val)){
                p2 = p2->next;
                p = p->next;
            }
            if(!p1 || !p2){
                break;
            }
            p->next = p1;
            p1 = p1->next;
            p = p->next;
            flag = 1;            
        }
    }
    if(p1){
        p->next = p1;
    }
    if(p2){
        p->next = p2;
    }
    return head;    
}
