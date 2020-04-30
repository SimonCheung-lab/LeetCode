/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* head = (struct ListNode*)malloc(sizeof(struct ListNode));
    head->val = 0;
    head->next = NULL;

    struct ListNode* p = head;
    int sum = l1->val + l2->val;
    p->val = sum % 10;
    sum /= 10;

    struct ListNode* pl1, *pl2;
    pl1 = l1->next;
    pl2 = l2->next;

    while (pl1 && pl2){
        p->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        p = p->next;
        sum += pl1->val + pl2->val;
        p->val = sum % 10;
        sum /= 10;
        pl1 = pl1->next;
        pl2 = pl2->next;
    }

    while (pl1){
        p->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        p = p->next;
        sum += pl1->val;
        p->val = sum % 10;
        sum /= 10;
        pl1 = pl1->next;
    }

    while (pl2){
        p->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        p = p->next;
        sum += pl2->val;
        p->val = sum % 10;
        sum /= 10;
        pl2 = pl2->next;
    }

    if (sum > 0){
        p->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        p = p->next;
        p->val = sum;
    }

    p->next = NULL;

    return head;
}
